# app/pipeline/preprocess/image_preprocessor.py
# 图像预处理模块 - 印章检测与去除
# 从 pdf_ocr_processor.py 拆分

import cv2
import numpy as np
from ...utils import log_with_timestamp


class ImagePreprocessor:
    """图像预处理器 - 印章检测与去除"""
    
    @staticmethod
    def analyze_channel_quality(img, channel_img, channel_name):
        """
        分析通道质量：计算对比度、清晰度等指标
        
        Args:
            img: 原始BGR图像
            channel_img: 单通道图像
            channel_name: 通道名称
            
        Returns:
            dict: 包含对比度、清晰度、动态范围、综合评分的字典
        """
        # 计算标准差（对比度指标）
        std_dev = np.std(channel_img)
        
        # 计算边缘强度（清晰度指标）
        edges = cv2.Canny(channel_img, 50, 150)
        edge_density = np.sum(edges > 0) / edges.size
        
        # 计算直方图分布（动态范围）
        hist = cv2.calcHist([channel_img], [0], None, [256], [0, 256])
        dynamic_range = np.sum(hist > 0)
        
        return {
            'name': channel_name,
            'contrast': std_dev,
            'clarity': edge_density,
            'dynamic_range': dynamic_range,
            'score': std_dev * 0.5 + edge_density * 5000 + dynamic_range * 0.1
        }

    @staticmethod
    def detect_seal_color(img):
        """
        检测印章主要颜色
        
        Args:
            img: BGR格式的OpenCV图像
            
        Returns:
            tuple: (印章颜色 'red'/'blue'/'black'/'unknown', 印章占比)
        """
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # 检测红色印章区域
        red_mask1 = cv2.inRange(img_hsv, (0, 100, 100), (10, 255, 255))
        red_mask2 = cv2.inRange(img_hsv, (170, 100, 100), (180, 255, 255))
        red_mask = red_mask1 + red_mask2
        red_ratio = np.sum(red_mask > 0) / red_mask.size
        
        # 检测蓝色印章
        blue_mask = cv2.inRange(img_hsv, (100, 100, 100), (130, 255, 255))
        blue_ratio = np.sum(blue_mask > 0) / blue_mask.size
        
        # 检测黑色印章
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        black_mask = cv2.inRange(gray, 0, 50)
        black_ratio = np.sum(black_mask > 0) / black_mask.size
        
        if red_ratio > 0.005:
            return 'red', red_ratio
        elif blue_ratio > 0.005:
            return 'blue', blue_ratio
        elif black_ratio > 0.05:
            return 'black', black_ratio
        else:
            return 'unknown', 0

    def select_best_channel_for_seal_removal(self, img):
        """
        移除印章：根据印章颜色智能选择最优通道
        
        Args:
            img: BGR格式的OpenCV图像
            
        Returns:
            tuple: (best_channel, seal_color, seal_ratio)
        """
        # 分离RGB通道
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        r_channel = img_rgb[:, :, 0]
        g_channel = img_rgb[:, :, 1]
        b_channel = img_rgb[:, :, 2]
        
        channels = {
            'R通道': r_channel, 'G通道': g_channel, 'B通道': b_channel
        }
        
        seal_color, seal_ratio = self.detect_seal_color(img)
        log_with_timestamp(f"  [Pre-process] 检测到 {seal_color} 色印章 (占比{seal_ratio*100:.2f}%)")
        
        if seal_color == 'red':
            # 红色印章 -> R通道 (红章在R通道最浅)
            best_channel = r_channel
        elif seal_color == 'blue':
            # 蓝色印章 -> B通道 (蓝章在B通道最浅)
            best_channel = b_channel
        else:
            # 未检测到特定印章，使用评分系统
            channel_scores = {}
            for name, channel in channels.items():
                quality = self.analyze_channel_quality(img, channel, name)
                channel_scores[name] = quality
            
            best_channel_name = max(channel_scores, key=lambda x: channel_scores[x]['score'])
            best_channel = channels[best_channel_name]
            log_with_timestamp(f"  [Auto-Select] 自动选择通道: {best_channel_name}")

        return best_channel, seal_color, seal_ratio

    def preprocess_image_for_ocr(self, img_cv):
        """
        对图像进行预处理以优化OCR识别
        
        1. 自动方向矫正 (0/180度)
        2. 智能判断是否需要去印章
        
        Args:
            img_cv: BGR格式的OpenCV图像
            
        Returns:
            tuple: (处理后的图像bytes, 是否进行了预处理)
        """
        try:
            is_processed = False
            current_img = img_cv
            
            # 1. 方向检测与矫正
            try:
                from .orientation_detector import OrientationDetector
                detector = OrientationDetector()
                current_img, rotated, debug_info = detector.process_image(current_img)
                if rotated:
                    is_processed = True
            except Exception as e:
                log_with_timestamp(f"  [WARN] 方向检测模块异常: {e}")

            # 2. 印章检测
            # 先检测印章比例
            seal_color, seal_ratio = self.detect_seal_color(current_img)
            
            # 阈值：如果印章占比超过 0.5%，则进行去印章处理
            if seal_ratio > 0.005:
                # log_with_timestamp(f"  [Decision] 印章占比 {seal_ratio*100:.2f}% > 0.5%，启用预处理...")
                
                # 选择最佳通道
                best_channel, _, _ = self.select_best_channel_for_seal_removal(current_img)
                
                # 直接使用最佳通道（不进行二值化，保留更多细节）
                _, encoded_img = cv2.imencode('.png', best_channel)
                return encoded_img.tobytes(), True
            else:
                # log_with_timestamp(f"  [Decision] 印章占比 {seal_ratio*100:.2f}% (微量/无)，使用原图以获得最佳质量")
                
                # 如果只是旋转了，也需要返回编码后的图片
                if is_processed:
                    _, encoded_img = cv2.imencode('.png', current_img)
                    return encoded_img.tobytes(), True
                    
                # 保持原图 - 返回None表示使用原始PNG数据
                return None, False
                
        except Exception as e:
            log_with_timestamp(f"  [WARN] 图像预处理异常，使用原图: {e}")
            return None, False


# 便捷函数
def detect_seal_color(img):
    """检测印章颜色的便捷函数"""
    return ImagePreprocessor.detect_seal_color(img)


def preprocess_for_ocr(img_cv):
    """图像预处理的便捷函数"""
    preprocessor = ImagePreprocessor()
    return preprocessor.preprocess_image_for_ocr(img_cv)
