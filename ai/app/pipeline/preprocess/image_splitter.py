import os
import sys
import cv2
import numpy as np
import math

# 添加项目根目录到路径，以便导入 app 包
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, project_root)

from app.utils import log_with_timestamp

class ImageSplitter:
    """处理双页扫描图片的检测与拆分"""
    
    def __init__(self, ocr_client=None):
        """
        初始化
        Args:
            ocr_client: OCR客户端实例，用于调用VL大模型
        """
        self.ocr_client = ocr_client
        self.debug_dir = None  # 用于保存调试图片的目录

    def set_debug_dir(self, debug_dir):
        """设置调试目录"""
        self.debug_dir = debug_dir


    def _read_image(self, path):
        """读取图片 (支持中文路径)"""
        try:
            return cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
        except Exception as e:
            log_with_timestamp(f"读取图片失败: {path}, {e}")
            return None

    def _save_image(self, path, img):
        """保存图片 (支持中文路径)"""
        try:
            cv2.imencode(os.path.splitext(path)[1], img)[1].tofile(path)
            return True
        except Exception as e:
            log_with_timestamp(f"保存图片失败: {path}, {e}")
            return False

    def check_is_double_page(self, image_path, image_cv=None):
        """
        检查是否疑似双页扫描
        
        Args:
            image_path: 图片路径
            image_cv: OpenCV图像对象 (可选，避免重复读取)
            
        Returns:
            bool: 是否疑似双页
        """
        if image_cv is None:
            image_cv = self._read_image(image_path)
            if image_cv is None:
                return False
                
        h, w = image_cv.shape[:2]
        ratio = w / h
        
        # 宽一定大于高，且比例通常在 1.25 以上 (两个A4竖放是 ~1.414)
        is_wide = ratio > 1.2
        
        if is_wide:
            log_with_timestamp(f"检测到宽图 (宽高比 {ratio:.2f})，疑似双页扫描: {os.path.basename(image_path)}")
        
        return is_wide

    def detect_split_line(self, image_path, image_cv=None, default_ratio=0.5):
        """
        检测分割线 x 坐标
        
        Args:
            image_path: 图片路径
            image_cv: OpenCV图片
            default_ratio: 默认分割比例
            
        Returns:
            int: 分割线x坐标
        """
        if image_cv is None:
            image_cv = self._read_image(image_path)
        
        h, w = image_cv.shape[:2]
        basename = os.path.basename(image_path)
        
        # 1. VL 模型粗定位 (获取比例)
        vl_ratio = default_ratio
        if self.ocr_client:
            try:
                #prompt = "这是一张双页扫描的合同文件。请判断左右两页的分界线位置。请返回分界线相对于图片宽度的比例（0.0 到 1.0 之间的小数）。不要解释，只返回数字。"
                # 调用VL模型 (需确保 client 实现了 call_vl_chat)
                #vl_response = self.ocr_client.call_vl_chat(image_path, prompt)
                
                # 解析响应
                import re
                match = True
                #match = re.search(r"0\.\d+", vl_response)
                if match:
                    #vl_ratio = float(match.group())
                    vl_ratio = 0.49  # 临时硬编码测试
                    log_with_timestamp(f"VL 模型建议分割比例: {vl_ratio}")
                else:
                    #log_with_timestamp(f"VL 模型返回无法解析: {vl_response}，使用默认比例: {default_ratio}")
                    pass
                    
            except Exception as e:
                log_with_timestamp(f"VL 模型识别失败: {e}，使用默认比例")
        
        vl_split_x = int(w * vl_ratio)
        
        # 2. CV 算法精确定位 (基于轮廓和色块)
        cv_split_x = self._detect_split_x_by_contours(image_cv, vl_split_x)
        
        if cv_split_x:
            final_ratio = cv_split_x / w
            log_with_timestamp(f"分割对比 - VL建议: {vl_ratio:.4f} (x={vl_split_x}) | CV修正: {final_ratio:.4f} (x={cv_split_x})")
            
            # 简单校验：如果 CV 结果偏离 VL 太多 (>20%)，可能 CV 找错了
            if abs(cv_split_x - vl_split_x) > w * 0.2:
                log_with_timestamp("⚠️ CV 结果与 VL 建议偏差过大，回退使用 VL 建议")
                return vl_split_x
            return cv_split_x
        else:
            log_with_timestamp("CV 无法确定分割线，使用 VL 建议")
            return vl_split_x

    def _detect_split_x_by_contours(self, img, hint_x):
        """
        使用轮廓分析寻找左右两个主要内容块
        """
        try:
            h, w = img.shape[:2]
            
            # 转灰度
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # 高斯模糊去除噪点
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            
            # 二值化 / Canny
            # 使用 Otsu 自动阈值
            _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            
            # 膨胀操作，让文字块连成整体
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
            dilated = cv2.dilate(binary, kernel, iterations=2)
            
            # 查找轮廓
            contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # 筛选大轮廓 (面积 > 图片面积 10%)
            valid_contours = []
            min_area = w * h * 0.05
            
            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > min_area:
                    x, y, cw, ch = cv2.boundingRect(cnt)
                    # 必须要有一定的高度
                    if ch > h * 0.5:
                        valid_contours.append((x, y, cw, ch, area))
            
            # 按 x 坐标排序
            valid_contours.sort(key=lambda c: c[0])
            
            # if self.debug_dir:
            #     try:
            #         debug_img = img.copy()
            #         for x, y, cw, ch, area in valid_contours:
            #             cv2.rectangle(debug_img, (x, y), (x+cw, y+ch), (0, 255, 0), 2)
            #         self._save_image(os.path.join(self.debug_dir, "debug_contours.jpg"), debug_img)
            #     except:
            #         pass

            # 如果找到了两个主要的大轮廓
            if len(valid_contours) >= 2:
                # 寻找在 hint_x 左右两侧最大的两个
                left_candidates = [c for c in valid_contours if c[0] + c[2] < hint_x + w*0.1] # 左侧结束点在中间偏左
                right_candidates = [c for c in valid_contours if c[0] > hint_x - w*0.1] # 右侧开始点在中间偏右
                
                if left_candidates and right_candidates:
                    # 取最靠中间的左块和最靠中间的右块
                    left_block = max(left_candidates, key=lambda c: c[0] + c[2]) # 最靠右的
                    right_block = min(right_candidates, key=lambda c: c[0])      # 最靠左的
                    
                    l_end = left_block[0] + left_block[2]
                    r_start = right_block[0]
                    
                    # 分割线取中间
                    return (l_end + r_start) // 2
            
            # 如果轮廓分析未返回结果，或者为了进一步验证，使用垂直投影寻找中缝（深色竖线）
            search_range = int(w * 0.15) # 搜索范围扩大到 15%
            start_x = max(0, hint_x - search_range)
            end_x = min(w, hint_x + search_range)
            
            if start_x >= end_x:
                return None

            # 裁剪出中间区域进行分析
            roi = gray[:, start_x:end_x]
            
            #垂直投影：计算每一列的平均像素值
            # axis=0 表示沿垂直方向压缩，得到一行数据
            col_means = np.mean(roi, axis=0)
            
            # 平滑曲线，消除噪点影响
            kernel_size = 15
            smoothed_means = cv2.GaussianBlur(col_means.reshape(1, -1), (kernel_size, 1), 0).flatten()
            
            # 寻找极小值点 (最暗的位置) 和 极大值点 (最亮的位置)
            min_idx = np.argmin(smoothed_means)
            max_idx = np.argmax(smoothed_means)
            
            min_val = smoothed_means[min_idx]
            max_val = smoothed_means[max_idx]
            
            # 判断逻辑：
            # 1. 如果 min_val 足够暗 (例如 < 150)，通常是书本的中缝阴影或黑线 -> 使用 min_idx
            # 2. 如果 min_val 很亮 (> 200)，说明是白底 scan，中间可能是白色的间隔 -> 使用 max_idx
            # 3. 如果介于两者之间，优先看哪个更像"极值" (比周围显著更暗或更亮)
            
            use_dark_valley = True
            if min_val > 150: # 如果最暗的地方也是灰色的，可能不是黑缝
                use_dark_valley = False
                log_with_timestamp(f"CV 投影分析: 最暗值 ({min_val:.1f}) 不够黑，尝试寻找白色间隙")
            
            best_split_x = -1
            
            if use_dark_valley:
                best_split_x = start_x + min_idx
                log_with_timestamp(f"CV 垂直投影分析: 搜索范围 [{start_x}, {end_x}], 锁定暗缝位于 {best_split_x} (val={min_val:.1f})")
                
                # 检查波谷：中缝应该显著比两边暗
                check_dist = int(w * 0.05)
                left_check_idx = max(0, min_idx - check_dist)
                right_check_idx = min(len(smoothed_means) - 1, min_idx + check_dist)
                
                val_left = smoothed_means[left_check_idx]
                val_right = smoothed_means[right_check_idx]
                
                if min_val < val_left and min_val < val_right:
                    return best_split_x
                else:
                    log_with_timestamp(f"CV 投影暗缝未形成明显波谷 (min:{min_val:.1f}, L:{val_left:.1f}, R:{val_right:.1f})，尝试白色间隙")
                    use_dark_valley = False # 失败回退到找白缝

            if not use_dark_valley:
                # 寻找最亮的地方 (白色间隙)
                best_split_x = start_x + max_idx
                log_with_timestamp(f"CV 垂直投影分析: 锁定白缝位于 {best_split_x} (val={max_val:.1f})")
                
                # 检查波峰：中间应该显著比两边亮 (或者是平台)
                # 注意：如果全是白的，max_val 可能等于 min_val 或者差不多
                if max_val < 200: # 如果最亮的地方都很暗，那这就不是白缝
                     log_with_timestamp(f"CV 投影最亮值 ({max_val:.1f}) 过暗，放弃")
                     return None
                     
                return best_split_x
            
            return None
        except Exception as e:
           log_with_timestamp(f"CV分析出错: {e}")
           return None

    def split_and_save(self, image_path, split_x, output_dir=None):
        """
        拆分并保存图片
        
        Args:
            image_path: 原图路径
            split_x: 分割线x坐标
            output_dir: 输出目录，默认为原图所在目录
            
        Returns:
            list: [path1, path2]
        """
        img = self._read_image(image_path)
        if img is None:
            return [image_path] # 失败返回原图
            
        h, w = img.shape[:2]
        
        # 简单边界检查
        if split_x < 50 or split_x > w - 50:
             log_with_timestamp(f"分割线位置异常 ({split_x})，跳过拆分")
             return [image_path]
             
        left_img = img[:, :split_x]
        right_img = img[:, split_x:]
        
        dir_name = output_dir if output_dir else os.path.dirname(image_path)
        basename = os.path.splitext(os.path.basename(image_path))[0]
        #ext = os.path.splitext(image_path)[1]
        ext = ".png" # 强制保存为png，避免格式问题
        
        # 构造新文件名
        # 注意：这里需要考虑与现有命名规范的兼容，建议使用 _p1, _p2 后缀
        path1 = os.path.join(dir_name, f"{basename}_p1{ext}")
        path2 = os.path.join(dir_name, f"{basename}_p2{ext}")
        
        self._save_image(path1, left_img)
        self._save_image(path2, right_img)
        
        log_with_timestamp(f"图片已拆分: {os.path.basename(image_path)} -> {os.path.basename(path1)}, {os.path.basename(path2)}")
        
        return [path1, path2]

if __name__ == '__main__':
    # 测试代码
    print("开始测试 ImageSplitter...")
    
    # 模拟 OCR Client
    class MockOCRClient:
        def call_vl_chat(self, image_path, prompt):
            print(f"Mock VL Call: {prompt}")
            return "0.49" # 模拟返回
        
    for x in range(len(os.listdir(r"D:\新建文件夹\合同分析的第八版 20251213\uploads\1 智造谷产业服务综合体项目合同协议书_OCR\images"))): 
                
        #test_path = r"D:\新建文件夹\合同分析的第八版 20251213\uploads\1 智造谷产业服务综合体项目合同协议书_OCR\images\1.png"
    
        test_path = f"D:/新建文件夹/合同分析的第八版 20251213/uploads/1 智造谷产业服务综合体项目合同协议书_OCR/images/{x+1}.png"
        
        if os.path.exists(test_path):
            splitter = ImageSplitter(MockOCRClient())
            
            # 设置 debug 目录到同级
            debug_dir = os.path.dirname(test_path)
            splitter.set_debug_dir(debug_dir)
            
            if splitter.check_is_double_page(test_path):
                print("检测到双页")
                split_x = splitter.detect_split_line(test_path)
                print(f"分割线位置: {split_x}")
                
                paths = splitter.split_and_save(test_path, split_x)
                print(f"生成文件: {paths}")
            else:
                print("未检测到双页特征")
        else:
            print(f"测试文件不存在: {test_path}")
