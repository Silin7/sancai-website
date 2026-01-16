# app/pipeline/preprocess/pdf_ocr_processor.py
# PDF OCR处理器 - 处理纯图片PDF的OCR转换
import os
import json
import hashlib
import base64
from datetime import datetime
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image
import io
import shutil
import random
import cv2
import numpy as np

from ...utils import log_with_timestamp, push_sse_event
from ...config import Config

# 导入拆分出的模块
from .ocr_api_client import DashScopeOCRClient
from .image_preprocessor import ImagePreprocessor
from .image_splitter import ImageSplitter
from ...config import Config


# 添加python-docx导入
try:
    from docx import Document
    from docx.shared import Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.shared import Pt
    from docx.enum.style import WD_STYLE_TYPE
    DOCX_AVAILABLE = True
except ImportError:
    log_with_timestamp("python-docx库未安装，DOCX生成功能将不可用")
    DOCX_AVAILABLE = False

class PDFOCRProcessor:
    """PDF OCR处理器 - 重新设计文件夹结构"""
    
    def __init__(self, 
                 save_debug_comparison=False,   # 保存对比图 (原图/最佳通道/处理结果)
                 save_original_png=False,       # 保存原始PNG到debug目录
                 save_sent_png=False,           # 保存实际发送给OCR的PNG
                 save_ocr_txt=False,            # 保存OCR结果为TXT文件
                 doc_type=None):                # 🆕 文档类型
        """
        初始化PDF OCR处理器
        
        Args:
            save_debug_comparison: 是否保存matplotlib对比图 (原图/最佳通道/处理结果)
            save_original_png: 是否保存原始PNG到debug目录
            save_sent_png: 是否保存实际发送给OCR的图片
            save_ocr_txt: 是否保存OCR结果为TXT文件
            doc_type: 文档类型 ('award', 'bid', etc.)
        """
        self.doc_type = doc_type
        self.config = Config.get_ocr_config(doc_type=doc_type)
        self.upload_dir = Config.UPLOAD_FOLDER
        self.ocr_cache_mapping_file = Config.OCR_CACHE_FILE
        
        # 调试功能开关
        self.save_debug_comparison = save_debug_comparison
        self.save_original_png = save_original_png
        self.save_sent_png = save_sent_png
        self.save_ocr_txt = save_ocr_txt
        
        # 初始化拆分模块实例
        self._image_preprocessor = ImagePreprocessor()
        self._ocr_client = DashScopeOCRClient(self.config, doc_type=doc_type)
        self._image_splitter = ImageSplitter(self._ocr_client)
        
        # 确保上传目录存在
        os.makedirs(self.upload_dir, exist_ok=True)
        
        # 初始化OCR缓存映射
        self._init_ocr_mapping()
    
    def _init_ocr_mapping(self):
        """初始化OCR缓存映射文件"""
        if not os.path.exists(self.ocr_cache_mapping_file):
            with open(self.ocr_cache_mapping_file, 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False, indent=2)
    
    # ========== 印章预处理方法 (委托给 ImagePreprocessor) ==========
    
    @staticmethod
    def analyze_channel_quality(img, channel_img, channel_name):
        """分析通道质量 - 委托给 ImagePreprocessor"""
        return ImagePreprocessor.analyze_channel_quality(img, channel_img, channel_name)

    @staticmethod
    def detect_seal_color(img):
        """检测印章主要颜色 - 委托给 ImagePreprocessor"""
        return ImagePreprocessor.detect_seal_color(img)

    def select_best_channel_for_seal_removal(self, img):
        """移除印章：根据印章颜色智能选择最优通道 - 委托给 ImagePreprocessor"""
        return self._image_preprocessor.select_best_channel_for_seal_removal(img)

    def preprocess_image_for_ocr(self, img_cv):
        """对图像进行预处理以优化OCR识别 - 委托给 ImagePreprocessor"""
        return self._image_preprocessor.preprocess_image_for_ocr(img_cv)

    # ========== 印章预处理方法结束 ==========
    
    # ========== DeepSeek OCR 相关方法 ==========
    
    @staticmethod
    def extract_plain_text(ocr_text):
        """
        从 DeepSeek OCR 结果中提取纯文字，过滤坐标标签
        
        DeepSeek OCR 返回格式: <|ref|>文字<|/ref|><|det|>[[x1,y1,x2,y2]]<|/det|>
        此方法移除所有标签，只保留纯文字
        
        Args:
            ocr_text: 带坐标标签的 OCR 结果
            
        Returns:
            str: 纯文字内容
        """
        import re
        if not ocr_text:
            return ""
        
        # 移除 <|ref|>...<|/ref|> 标签，保留内容
        text = re.sub(r'<\|ref\|>(.*?)<\|/ref\|>', r'\1', ocr_text)
        # 移除 <|det|>...<|/det|> 标签及其内容（坐标信息）
        text = re.sub(r'<\|det\|>\[\[.*?\]\]<\|/det\|>', '', text)
        # 移除其他可能的标签
        text = re.sub(r'<\|[^|]+\|>', '', text)
        
        return text.strip()
    
    @staticmethod
    def parse_grounding_result(ocr_text):
        """
        解析带坐标的 DeepSeek OCR 结果
        
        Args:
            ocr_text: 带坐标标签的 OCR 结果
            
        Returns:
            list: [{text: str, bbox: [x1,y1,x2,y2]}, ...]
        """
        import re
        results = []
        
        # 匹配 <|ref|>文字<|/ref|><|det|>[[x1,y1,x2,y2]]<|/det|> 格式
        pattern = r'<\|ref\|>(.*?)<\|/ref\|><\|det\|>\[\[(\d+),(\d+),(\d+),(\d+)\]\]<\|/det\|>'
        matches = re.findall(pattern, ocr_text)
        
        for match in matches:
            text = match[0].strip()
            x1, y1, x2, y2 = int(match[1]), int(match[2]), int(match[3]), int(match[4])
            results.append({
                'text': text,
                'bbox': [x1, y1, x2, y2]
            })
        
        return results
    
    def call_deepseek_ocr(self, image_path, max_retries=10, with_grounding=True):
        """
        调用 DeepSeek OCR (Ollama) 进行 OCR
        
        Args:
            image_path: 图像文件路径
            max_retries: 最大重试次数
            with_grounding: 是否启用坐标模式（默认 True）
            
        Returns:
            dict: OCR结果，包含 text（纯文字）和 text_with_bbox（带坐标原始结果）
        """
        import requests
        import time
        
        last_error = None
        
        for attempt in range(max_retries):
            try:
                # 读取图片并编码为 base64
                with open(image_path, "rb") as f:
                    image_base64 = base64.b64encode(f.read()).decode('utf-8')
                
                # 选择 prompt
                if with_grounding:
                    prompt = "<|grounding|>OCR this image."
                else:
                    prompt = "Free OCR."
                
                # 构建请求
                payload = {
                    "model": self.config['model'],
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt,
                            "images": [image_base64]
                        }
                    ],
                    "stream": False,
                    "options": {
                        "num_predict": 8192
                    }
                }
                
                url = f"{self.config['api_base']}/api/chat"
                log_with_timestamp(f"调用 DeepSeek OCR: {os.path.basename(image_path)} (尝试 {attempt + 1}/{max_retries})")
                
                response = requests.post(
                    url,
                    json=payload,
                    timeout=self.config['timeout']
                )
                
                if response.status_code == 200:
                    result = response.json()
                    ocr_text_raw = ""
                    
                    if 'message' in result and 'content' in result['message']:
                        ocr_text_raw = result['message']['content']
                    elif 'response' in result:
                        ocr_text_raw = result['response']
                    
                    # 提取纯文字
                    ocr_text_plain = self.extract_plain_text(ocr_text_raw) if with_grounding else ocr_text_raw
                    
                    log_with_timestamp(f"DeepSeek OCR 成功: {os.path.basename(image_path)} - {len(ocr_text_plain)} 字符")
                    
                    return {
                        'success': True,
                        'text': ocr_text_plain,  # 纯文字（用于 DOCX）
                        'text_with_bbox': ocr_text_raw if with_grounding else None,  # 带坐标原始结果
                        'image_path': image_path,
                        'page_number': int(os.path.splitext(os.path.basename(image_path))[0]),
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'provider': 'deepseek_ollama',
                        'retry_count': attempt
                    }
                else:
                    last_error = f"DeepSeek OCR 请求失败: {response.status_code}"
                    log_with_timestamp(f"{last_error} - 尝试 {attempt + 1}/{max_retries}")
                    
            except requests.exceptions.Timeout:
                last_error = f"DeepSeek OCR 请求超时 (>{self.config['timeout']}秒)"
                log_with_timestamp(f"{last_error} - 尝试 {attempt + 1}/{max_retries}")
            except Exception as e:
                last_error = f"DeepSeek OCR 处理失败: {str(e)}"
                log_with_timestamp(f"{last_error} - 尝试 {attempt + 1}/{max_retries}")
            
            # 重试等待
            if attempt < max_retries - 1:
                wait_time = min(2 ** attempt, 60)
                time.sleep(wait_time)
        
        # 所有重试失败
        return {
            'success': False,
            'error': last_error,
            'image_path': image_path,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'provider': 'deepseek_ollama',
            'retry_count': max_retries
        }
    
    def call_ocr(self, image_path, max_retries=10):
        """
        统一 OCR 调用入口，根据 provider 选择不同的 OCR 服务
        
        Args:
            image_path: 图像文件路径
            max_retries: 最大重试次数
            
        Returns:
            dict: OCR结果
        """
        provider = self.config.get('provider', 'dashscope')
        
        if provider == 'deepseek_ollama':
            return self.call_deepseek_ocr(image_path, max_retries)
        else:
            # 默认使用 DashScope
            return self.call_dashscope_ocr(image_path, max_retries)
    
    # ========== DeepSeek OCR 相关方法结束 ==========

    def _create_lightweight_cache_entry(self, final_result):
        """
        创建精简版的缓存条目，只保留索引和统计信息
        
        ocr_cache_mapping.json 的作用是快速索引，不需要保存完整数据。
        完整数据已经保存在 OCR 文件夹的以下文件中：
        - complete_ocr_result.json: 包含完整的 combined_text 和 page_results
        - {i}_ocr_result.json: 每页的详细 OCR 结果
        
        缓存映射只需保留：
        1. 文件识别信息：file_md5, original_filename, pdf_filename
        2. 路径信息：ocr_folder, images_folder
        3. 统计信息：total_pages, success_pages, failed_pages
        4. 元数据：extraction_time, cached 等
        
        Args:
            final_result: 完整的OCR处理结果
            
        Returns:
            dict: 精简后的缓存条目（只包含索引信息）
        """
        # 只保留索引和统计信息
        lightweight_entry = {
            'success': final_result.get('success', True),
            'cached': final_result.get('cached', False),
            'file_md5': final_result.get('file_md5'),
            'original_filename': final_result.get('original_filename'),
            'pdf_filename': final_result.get('pdf_filename'),
            'total_pages': final_result.get('total_pages', 0),
            'success_pages': final_result.get('success_pages', 0),
            'failed_pages': final_result.get('failed_pages', 0),
            'extraction_time': final_result.get('extraction_time'),
            'ocr_folder': final_result.get('ocr_folder'),
            'images_folder': final_result.get('images_folder'),
        }
        
        # 可选字段
        if 'docx_info' in final_result:
            lightweight_entry['docx_info'] = final_result['docx_info']
        
        return lightweight_entry

    def _load_ocr_mapping(self):
        """加载OCR缓存映射"""
        try:
            with open(self.ocr_cache_mapping_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def _save_ocr_mapping(self, mapping):
        """保存OCR缓存映射"""
        with open(self.ocr_cache_mapping_file, 'w', encoding='utf-8') as f:
            json.dump(mapping, f, ensure_ascii=False, indent=2)
    
    def _calculate_file_md5(self, file_path):
        """计算文件MD5值"""
        hash_md5 = hashlib.md5()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            log_with_timestamp(f"计算文件MD5失败 {file_path}: {e}")
            return None
    
    def _get_ocr_folder_path(self, pdf_path, original_filename):
        """
        根据PDF文件名和上传文件名变更逻辑，获取OCR文件夹路径
        
        Args:
            pdf_path: PDF文件路径
            original_filename: 原始文件名
            
        Returns:
            str: OCR文件夹路径
        """
        # 获取实际存储的PDF文件名（重命名后的）
        actual_filename = os.path.basename(pdf_path)
        # 移除扩展名
        filename_without_ext = os.path.splitext(actual_filename)[0]
        # 创建OCR文件夹名称：文件名_OCR
        ocr_folder_name = f"{filename_without_ext}_OCR"
        ocr_folder_path = os.path.join(self.upload_dir, ocr_folder_name)
        return ocr_folder_path
    
    def _get_images_subfolder_path(self, ocr_folder_path):
        """获取images子文件夹路径"""
        return os.path.join(ocr_folder_path, "images")
    
    def _check_and_split_image(self, image_path, debug_dir):
        """
        检查并处理双页拆分
        
        Args:
            image_path: 图片路径
            debug_dir: 调试目录
            
        Returns:
            list: 处理后的图片路径列表 (原图或拆分后的两张图)
        """
        try:
            if self._image_splitter.check_is_double_page(image_path):
                base = os.path.splitext(image_path)[0]
                # 检查拆分文件是否已存在 (Optimization) - 假设 .png 后缀
                p1 = f"{base}_p1.png"
                p2 = f"{base}_p2.png"
                
                # 如果两个拆分文件都存在，直接使用
                if os.path.exists(p1) and os.path.exists(p2):
                     log_with_timestamp(f"  [Split] 发现已有拆分结果，使用拆分文件: {os.path.basename(p1)}, {os.path.basename(p2)}")
                     return [p1, p2]

                log_with_timestamp(f"  [Split] 检测为双页，尝试拆分: {os.path.basename(image_path)}")
                self._image_splitter.set_debug_dir(debug_dir)
                split_x = self._image_splitter.detect_split_line(image_path)
                split_paths = self._image_splitter.split_and_save(image_path, split_x)
                
                if len(split_paths) == 2:
                    return split_paths
        except Exception as split_error:
             log_with_timestamp(f"  [WARN] 双页拆分处理失败: {split_error}")
        
        return [image_path]

    def extract_pdf_pages(self, pdf_path, output_dir, total_pages=None):
        """
        提取PDF每一页为图像文件 - 支持增量提取（跳过已存在的图片）
        集成印章预处理功能：自动检测印章并选择最佳通道
        
        Args:
            pdf_path: PDF文件路径
            output_dir: 输出目录
            total_pages: PDF总页数（用于检查）
            
        Returns:
            tuple: (image_paths列表, 是否有新提取的图片)
        """
        try:
            doc = fitz.open(pdf_path)
            image_paths = []
            extracted_new = False  # 标记是否有新提取的图片
            
            # 创建debug子目录（如果需要）
            debug_dir = os.path.join(output_dir, "debug")
            if self.save_debug_comparison or self.save_original_png or self.save_sent_png:
                os.makedirs(debug_dir, exist_ok=True)
            
            for page_num in range(len(doc)):
                image_filename = f"{page_num + 1}.png"
                image_path = os.path.join(output_dir, image_filename)
                
                # 检查图片是否已存在 - 但仍需检查是否需要拆分
                if os.path.exists(image_path):
                    log_with_timestamp(f"跳过已存在的图片: {image_filename}")
                    # 调用统一的拆分检查逻辑
                    processed_paths = self._check_and_split_image(image_path, debug_dir)
                    image_paths.extend(processed_paths)
                    continue
                
                # 提取页面为图像
                page = doc.load_page(page_num)
                
                # 🔍 DEBUG: 记录 PDF 原始尺寸
                pdf_rect = page.rect
                log_with_timestamp(f"  [尺寸] PDF 第{page_num + 1}页原始尺寸: {pdf_rect.width:.0f} x {pdf_rect.height:.0f} pts")
                
                mat = fitz.Matrix(2.0, 2.0)  # 2x缩放 (API会内部缩放，坐标基于内部尺寸)
                pix = page.get_pixmap(matrix=mat)
                img_data = pix.tobytes("png")
                
                # 🔍 DEBUG: 记录 pixmap 尺寸 (2x 缩放后)
                log_with_timestamp(f"  [尺寸] Pixmap 2x缩放后: {pix.width} x {pix.height} px")
                
                # 保存原始PNG（调试用）
                if self.save_original_png:
                    original_debug_path = os.path.join(debug_dir, f"{page_num + 1}_original.png")
                    with open(original_debug_path, 'wb') as f:
                        f.write(img_data)
                    log_with_timestamp(f"  [Debug] 保存原始图片: {page_num + 1}_original.png")
                
                # 尝试进行印章预处理
                try:
                    # 将PNG数据转换为OpenCV格式
                    nparr = np.frombuffer(img_data, np.uint8)
                    img_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                    
                    if img_cv is not None:
                        # 🔍 DEBUG: 记录 OpenCV 解码后的尺寸
                        log_with_timestamp(f"  [尺寸] OpenCV 解码后: {img_cv.shape[1]} x {img_cv.shape[0]} px (BGR)")
                        
                        # 1. 方向检测与矫正
                        rotated = False  # 初始化标志
                        try:
                            from .orientation_detector import OrientationDetector
                            detector = OrientationDetector()
                            # 传入 output_dir (images 目录) 作为调试目录
                            img_cv, rotated, debug_info = detector.process_image(img_cv, debug_dir=output_dir, image_name=str(page_num + 1))
                            if rotated:
                                log_with_timestamp(f"  [方向矫正] 第{page_num + 1}页: {debug_info}")
                        except Exception as orient_error:
                            log_with_timestamp(f"  [WARN] 方向检测异常: {orient_error}")
                        
                        # 2. 检测印章信息（用于调试对比图）
                        seal_color, seal_ratio = self.detect_seal_color(img_cv)
                        use_preprocessing = seal_ratio > 0.005
                        
                        if use_preprocessing:
                            # 选择最佳通道
                            best_channel, _, _ = self.select_best_channel_for_seal_removal(img_cv)
                            
                            # 🔍 DEBUG: 记录处理后的通道尺寸
                            log_with_timestamp(f"  [尺寸] 去印章通道: {best_channel.shape[1]} x {best_channel.shape[0]} px (灰度)")
                            
                            # 保存matplotlib对比图（调试用）
                            if self.save_debug_comparison:
                                try:
                                    import matplotlib
                                    matplotlib.use('Agg')  # 非交互式后端
                                    import matplotlib.pyplot as plt
                                    
                                    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
                                    axes[0].imshow(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
                                    axes[0].set_title(f'P{page_num + 1} - 原图')
                                    axes[1].imshow(best_channel, cmap='gray')
                                    axes[1].set_title(f'P{page_num + 1} - 最佳通道 ({seal_color}印章)')
                                    axes[2].imshow(best_channel, cmap='gray')
                                    axes[2].set_title(f'P{page_num + 1} - 处理结果')
                                    for ax in axes:
                                        ax.axis('off')
                                    plt.tight_layout()
                                    comparison_path = os.path.join(debug_dir, f"{page_num + 1}_comparison.png")
                                    plt.savefig(comparison_path, dpi=150)
                                    plt.close()
                                    log_with_timestamp(f"  [Debug] 保存对比图: {page_num + 1}_comparison.png")
                                except Exception as plot_error:
                                    log_with_timestamp(f"  [WARN] 保存对比图失败: {plot_error}")
                            
                            # 编码处理后的图片
                            _, encoded_img = cv2.imencode('.png', best_channel)
                            processed_data = encoded_img.tobytes()
                            
                            # 🔍 DEBUG: 记录最终保存的图片尺寸
                            log_with_timestamp(f"  [尺寸]  最终保存/发送给OCR: {best_channel.shape[1]} x {best_channel.shape[0]} px")
                            
                            # 保存实际发送的PNG（调试用）
                            if self.save_sent_png:
                                sent_debug_path = os.path.join(debug_dir, f"{page_num + 1}_sent_processed.png")
                                with open(sent_debug_path, 'wb') as f:
                                    f.write(processed_data)
                                log_with_timestamp(f"  [Debug] 保存发送图片: {page_num + 1}_sent_processed.png")
                            
                            # 保存预处理后的图片（用于OCR）
                            with open(image_path, 'wb') as f:
                                f.write(processed_data)
                            log_with_timestamp(f"提取第{page_num + 1}页图像(已去印章): {image_filename}")
                        else:
                            # 不需要去印章，但可能已被旋转
                            # 检查是否被旋转过（通过 rotated 变量）
                            if rotated:
                                # 保存旋转后的图片
                                _, encoded_img = cv2.imencode('.png', img_cv)
                                rotated_data = encoded_img.tobytes()
                                with open(image_path, 'wb') as f:
                                    f.write(rotated_data)
                                log_with_timestamp(f"提取第{page_num + 1}页图像(已旋转): {image_filename}")
                            else:
                                # 保存原图
                                if self.save_sent_png:
                                    sent_debug_path = os.path.join(debug_dir, f"{page_num + 1}_sent_original.png")
                                    with open(sent_debug_path, 'wb') as f:
                                        f.write(img_data)
                                    log_with_timestamp(f"  [Debug] 保存发送图片: {page_num + 1}_sent_original.png")
                                
                                pix.save(image_path)
                                log_with_timestamp(f"提取第{page_num + 1}页图像(原图): {image_filename}")
                    else:
                        # OpenCV无法解码，保存原图
                        pix.save(image_path)
                        log_with_timestamp(f"提取第{page_num + 1}页图像: {image_filename}")
                        
                except Exception as preprocess_error:
                    # 预处理失败，保存原图
                    log_with_timestamp(f"  [WARN] 第{page_num + 1}页预处理失败，使用原图: {preprocess_error}")
                    pix.save(image_path)
                
                # --- Double Page Split Logic (Refactored) ---
                processed_paths = self._check_and_split_image(image_path, debug_dir)
                image_paths.extend(processed_paths)
                extracted_new = True
            
            doc.close()
            new_count = sum(1 for _ in range(len(image_paths)) if extracted_new)
            log_with_timestamp(f"PDF页面提取完成，共{len(image_paths)}页，新提取{new_count if extracted_new else 0}页")
            return image_paths, extracted_new
            
        except Exception as e:
            log_with_timestamp(f"提取PDF页面失败 {pdf_path}: {e}")
            raise e
    
    def encode_image_to_base64(self, image_path):
        """将图像文件编码为base64字符串 - 委托给 OCR Client"""
        return self._ocr_client.encode_image_to_base64(image_path)
    
    def call_dashscope_ocr(self, image_path, max_retries=10):
        """
        调用阿里云DashScope API进行OCR - 委托给 OCR Client
        
        Args:
            image_path: 图像文件路径
            max_retries: 最大重试次数（默认10次）
            
        Returns:
            dict: OCR结果
        """
        return self._ocr_client.call_ocr(image_path, max_retries)
    
    def _check_cache_validity(self, ocr_folder_path, pdf_path, file_md5):
        """
        检查OCR缓存是否有效
        
        Args:
            ocr_folder_path: OCR文件夹路径
            pdf_path: PDF文件路径
            file_md5: 文件MD5
            
        Returns:
            dict: 缓存有效性检查结果
        """
        try:
            # 检查是否存在主JSON文件
            main_json_path = os.path.join(ocr_folder_path, "complete_ocr_result.json")
            docx_path = os.path.join(ocr_folder_path, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_完整版.docx")
            
            if not os.path.exists(main_json_path):
                return {'valid': False, 'reason': '主JSON文件不存在', 'missing': 'complete_ocr_result.json'}
            
            # 读取主JSON文件
            try:
                with open(main_json_path, 'r', encoding='utf-8') as f:
                    main_result = json.load(f)
            except (json.JSONDecodeError, IOError):
                return {'valid': False, 'reason': '主JSON文件损坏', 'missing': 'complete_ocr_result.json'}
            
            # 验证JSON文件完整性
            required_fields = ['file_md5', 'original_filename', 'total_pages', 'page_results', 'combined_text']
            for field in required_fields:
                if field not in main_result:
                    return {'valid': False, 'reason': f'主JSON文件缺少字段: {field}', 'missing': field}
            
            # 验证MD5是否匹配
            if main_result.get('file_md5') != file_md5:
                return {'valid': False, 'reason': 'MD5不匹配', 'missing': 'md5_mismatch'}
            
            # 检查每页的JSON文件是否存在且完整
            for i, page_result in enumerate(main_result.get('page_results', []), 1):
                page_json_path = os.path.join(ocr_folder_path, f"{i}_ocr_result.json")
                if not os.path.exists(page_json_path):
                    return {'valid': False, 'reason': f'第{i}页JSON文件不存在', 'missing': f'{i}_ocr_result.json'}
                
                try:
                    with open(page_json_path, 'r', encoding='utf-8') as f:
                        page_data = json.load(f)
                    if not page_data.get('success', False):
                        return {'valid': False, 'reason': f'第{i}页OCR处理失败', 'missing': f'page_{i}_failed'}
                except (json.JSONDecodeError, IOError):
                    return {'valid': False, 'reason': f'第{i}页JSON文件损坏', 'missing': f'{i}_ocr_result.json'}
            
            # 检查images文件夹
            images_folder = self._get_images_subfolder_path(ocr_folder_path)
            if not os.path.exists(images_folder):
                return {'valid': False, 'reason': 'images文件夹不存在', 'missing': 'images_folder'}
            
            # 检查DOCX文件是否存在
            if not os.path.exists(docx_path):
                return {'valid': False, 'reason': 'DOCX文件不存在', 'missing': 'docx_file', 'can_regenerate_docx': True}
            
            return {
                'valid': True, 
                'reason': '缓存有效',
                'main_result': main_result,
                'docx_exists': os.path.exists(docx_path)
            }
            
        except Exception as e:
            return {'valid': False, 'reason': f'缓存检查失败: {str(e)}', 'missing': 'unknown'}

    def _regenerate_docx_only(self, ocr_folder_path, pdf_path, main_result):
        """
        只重新生成DOCX文件（当OCR结果有效但DOCX文件缺失时）
        
        Args:
            ocr_folder_path: OCR文件夹路径
            pdf_path: PDF文件路径
            main_result: OCR处理结果
            
        Returns:
            dict: 处理结果
        """
        try:
            log_with_timestamp("检测到OCR结果有效，重新生成DOCX文件")
            docx_info = self._generate_docx_files(ocr_folder_path, main_result)
            
            if docx_info.get('docx_generated', False):
                # 更新主JSON文件中的DOCX信息
                main_result['docx_info'] = docx_info
                final_result_file = os.path.join(ocr_folder_path, "complete_ocr_result.json")
                with open(final_result_file, 'w', encoding='utf-8') as f:
                    json.dump(main_result, f, ensure_ascii=False, indent=2)
                
                log_with_timestamp("DOCX文件重新生成完成")
                return {
                    'success': True,
                    'cached': True,
                    'file_md5': main_result.get('file_md5'),
                    'result': main_result,
                    'folder_path': ocr_folder_path,
                    'docx_exists': True,
                    'regenerated_docx': True
                }
            else:
                return {
                    'success': False,
                    'error': f"DOCX重新生成失败: {docx_info.get('error', 'Unknown error')}",
                    'folder_path': ocr_folder_path
                }
        except Exception as e:
            return {
                'success': False,
                'error': f"DOCX重新生成异常: {str(e)}",
                'folder_path': ocr_folder_path
            }

    def _generate_docx_files(self, output_dir, final_result):
        """
        生成DOCX文件 - 只生成合并版本，不生成单页文件，不添加OCR信息页
        
        Args:
            output_dir: 输出目录（OCR文件夹根目录）
            final_result: OCR处理结果
            
        Returns:
            dict: 生成的DOCX文件信息
        """
        if not DOCX_AVAILABLE:
            log_with_timestamp("python-docx库不可用，跳过DOCX文件生成")
            return {
                'docx_generated': False,
                'error': 'python-docx库未安装'
            }
        
        try:
            docx_info = {
                'docx_generated': True,
                'merged_file': None,
                'generation_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # 使用PDF文件名
            pdf_filename = final_result.get('pdf_filename', 'document')
            base_name = os.path.splitext(pdf_filename)[0]
            
            # 获取成功的页面结果
            page_results = final_result.get('page_results', [])
            successful_pages = [p for p in page_results if p.get('success')]
            
            if not successful_pages:
                log_with_timestamp("没有成功的OCR结果，跳过DOCX生成")
                return {
                    'docx_generated': False,
                    'error': '没有成功的OCR结果'
                }
            
            # 在内存中创建DOCX文档
            merged_doc = Document()
            
            # 直接添加每页内容，不添加OCR信息页
            for i, page_result in enumerate(successful_pages):
                page_num = page_result.get('page_number', i + 1)
                page_text = page_result.get('text', '')
                
                if not page_text.strip():
                    continue
                
                # 添加页面内容（按段落分割）
                paragraphs = page_text.split('\n\n')
                for para_text in paragraphs:
                    if para_text.strip():
                        para = merged_doc.add_paragraph(para_text.strip())
                
                # 添加分页符（除了最后一页）
                if i < len(successful_pages) - 1:
                    merged_doc.add_page_break()
            
            # 设置文档样式
            for paragraph in merged_doc.paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run.font.size = Pt(12)
            
            # 保存合并的DOCX文件
            merged_filename = f"{base_name}_完整版.docx"
            merged_path = os.path.join(output_dir, merged_filename)
            merged_doc.save(merged_path)
            docx_info['merged_file'] = merged_path
            
            log_with_timestamp(f"生成DOCX文件: {merged_filename}")
            return docx_info
            
        except Exception as e:
            error_msg = f"DOCX文件生成失败: {str(e)}"
            log_with_timestamp(error_msg)
            return {
                'docx_generated': False,
                'error': error_msg
            }
    

    def process_pdf_with_ocr(self, pdf_path, original_filename, force_regenerate=False, user_id=None, project_id=None):
        """
        使用OCR处理PDF文件 - 增量处理版本
        
        特性：
        1. 图片提取：跳过已存在的图片
        2. OCR请求：跳过已有成功JSON的页面，失败的页面重试10次
        3. DOCX生成：只要有新提取图片或新OCR请求，就重新生成
        
        Args:
            pdf_path: PDF文件路径
            original_filename: 原始文件名
            force_regenerate: 是否强制重新生成
            user_id: 用户ID（用于SSE事件推送）
            project_id: 项目ID，用于更新后端状态存储
            
        Returns:
            dict: 处理结果
        """
        try:
            # 计算文件MD5
            file_md5 = self._calculate_file_md5(pdf_path)
            if not file_md5:
                raise Exception("无法计算文件MD5")
            
            # 获取OCR文件夹路径
            ocr_folder_path = self._get_ocr_folder_path(pdf_path, original_filename)
            images_folder = self._get_images_subfolder_path(ocr_folder_path)
            
            log_with_timestamp(f"开始OCR处理PDF: {original_filename} -> {os.path.basename(ocr_folder_path)}")
            
            # 如果强制重新生成，跳过缓存检查
            if not force_regenerate and os.path.exists(ocr_folder_path):
                cache_check = self._check_cache_validity(ocr_folder_path, pdf_path, file_md5)
                if cache_check['valid']:
                    log_with_timestamp(f"发现有效OCR缓存，直接使用现有结果: {original_filename}")
                    
                    # ===== 🆕 模拟OCR处理（用于测试/演示） =====
                    import time
                    SIMULATE_OCR = True  # 开关：设为 False 可关闭模拟
                    SIMULATE_DELAY = random.randint(20, 40)  # 每页模拟耗时(秒)
                    
                    if SIMULATE_OCR and user_id:
                        main_result = cache_check['main_result']
                        page_results = main_result.get('page_results', [])
                        total_pages = len(page_results)
                        
                        log_with_timestamp(f"[模拟OCR] 开始模拟处理 {total_pages} 页...")
                        
                        for i in range(1, total_pages + 1):
                            push_sse_event(user_id, 'ocr_progress', {
                                'filename': original_filename,
                                'file_md5': file_md5,
                                'current_page': i,
                                'total_pages': total_pages,
                                'message': f'正在处理第 {i}/{total_pages} 页...'
                            })
                            time.sleep(SIMULATE_DELAY)
                        
                        push_sse_event(user_id, 'ocr_complete', {
                            'filename': original_filename,
                            'total_pages': total_pages,
                            'success_pages': main_result.get('success_pages', total_pages),
                            'message': f'OCR转换完成！共处理 {total_pages} 页'
                        })
                        log_with_timestamp(f"[模拟OCR] 模拟完成")
                    # ===== 模拟结束 =====
                    
                    return {
                        'success': True,
                        'cached': True,
                        'file_md5': file_md5,
                        'result': cache_check['main_result'],
                        'folder_path': ocr_folder_path,
                        'docx_exists': cache_check.get('docx_exists', False),
                        'needs_docx_regenerate': False
                    }
            
            # 创建文件夹结构
            os.makedirs(ocr_folder_path, exist_ok=True)
            os.makedirs(images_folder, exist_ok=True)
            
            log_with_timestamp(f"创建OCR文件夹结构: {ocr_folder_path}")
            
            # 1. 提取PDF页面为图像（增量提取）
            image_paths, extracted_new_images = self.extract_pdf_pages(pdf_path, images_folder)
            total_pages = len(image_paths)
            
            # 2. 对每一页进行OCR处理（增量处理）
            ocr_results = []
            ocr_called = False  # 标记是否有新的OCR调用
            
            for i, image_path in enumerate(image_paths, 1):
                page_json_path = os.path.join(ocr_folder_path, f"{i}_ocr_result.json")
                
                # 检查是否已有成功的OCR结果
                if os.path.exists(page_json_path):
                    try:
                        with open(page_json_path, 'r', encoding='utf-8') as f:
                            existing_result = json.load(f)
                        if existing_result.get('success', False):
                            log_with_timestamp(f"跳过已有成功OCR结果: 第{i}页")
                            ocr_results.append(existing_result)
                            continue
                        else:
                            log_with_timestamp(f"发现失败的OCR结果，重新处理: 第{i}页")
                    except (json.JSONDecodeError, IOError):
                        log_with_timestamp(f"JSON文件损坏，重新处理: 第{i}页")
                
                # 需要进行OCR处理
                log_with_timestamp(f"处理第{i}/{total_pages}页...")
                # 推送OCR进度事件
                push_sse_event(user_id, 'ocr_progress', {
                    'filename': original_filename,
                    'file_md5': file_md5,
                    'current_page': i,
                    'total_pages': total_pages,
                    'message': f'正在处理第 {i}/{total_pages} 页...'
                })
                ocr_result = self.call_ocr(image_path, max_retries=10)  # 使用统一入口，根据 provider 选择
                ocr_result['page_number'] = i
                
                
                # 验证OCR结果：检查换行符合理性
                # A4文档通常每行约30-40个中文字符，如果文字较多但没有换行符，可能是识别异常
                if ocr_result.get('success', False):
                    ocr_text = ocr_result.get('text', '')
                    text_length = len(ocr_text.strip())
                    
                    # 阈值：50个字符（约1-2行A4文档的宽度）
                    # 如果文字超过50个字符但没有换行符，很可能是OCR异常
                    if '\n' not in ocr_text and text_length > 50:
                        log_with_timestamp(f"  ⚠️ 第{i}页OCR结果有{text_length}个字符但无换行符，标记为失败以便重试")
                        ocr_result['success'] = False
                        ocr_result['error'] = f'OCR结果无换行符（{text_length}字符，可能识别异常）'
                    elif '\n' not in ocr_text and text_length > 0:
                        log_with_timestamp(f"  ✓ 第{i}页为单行短文本({text_length}字符)，正常")
                
                
                ocr_results.append(ocr_result)
                ocr_called = True
                
                # 保存单页OCR结果
                with open(page_json_path, 'w', encoding='utf-8') as f:
                    json.dump(ocr_result, f, ensure_ascii=False, indent=2)
                
                # 保存OCR结果为TXT文件（调试用）
                # if self.save_ocr_txt and ocr_result.get('success', False):
                #     txt_path = os.path.join(ocr_folder_path, f"{i}_ocr_result.txt")
                #     with open(txt_path, 'w', encoding='utf-8') as f:
                #         f.write(ocr_result.get('text', ''))
                #     log_with_timestamp(f"  [Debug] 保存OCR文本: {i}_ocr_result.txt")
                
                
                
                # 🆕 检查是否被取消
                if user_id and project_id and file_md5:
                    from app.data_storage.file_metadata import check_ocr_cancellation
                    if check_ocr_cancellation(user_id, project_id, file_md5):
                        log_with_timestamp(f"🛑 OCR被用户终止: {original_filename} (第{i}页)")
                        
                        # 清除 OCR 状态
                        from app.data_storage.file_metadata import clear_file_ocr_status
                        clear_file_ocr_status(user_id, project_id, file_md5)
                        
                        return {
                            'success': False,
                            'error': 'OCR process cancelled by user',
                            'cancelled': True
                        }

                # 🆕 更新后端内存中的OCR状态（以便刷新页面后能恢复进度）
                if user_id and project_id and file_md5:
                    from app.data_storage.file_metadata import set_file_ocr_status
                    # 计算进度百分比
                    progress_percent = int((i / total_pages) * 100)
                    set_file_ocr_status(
                        user_id, project_id, file_md5, original_filename,
                        status='converting', 
                        progress=progress_percent,
                        message=f'正在处理第 {i}/{total_pages} 页...',
                        total_pages=total_pages,
                        current_page=i
                    )
            
            # 3. 合并所有页面的OCR结果
            combined_text = "\n".join([
                result['text'] for result in ocr_results 
                if result.get('success', False)
            ])
            
            final_result = {
                'success': True,
                'cached': False,
                'file_md5': file_md5,
                'original_filename': original_filename,
                'pdf_filename': os.path.basename(pdf_path),
                'total_pages': total_pages,
                'extraction_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'ocr_folder': ocr_folder_path,
                'images_folder': images_folder,
                'combined_text': combined_text,
                'page_results': ocr_results,
                'success_pages': len([r for r in ocr_results if r.get('success', False)]),
                'failed_pages': len([r for r in ocr_results if not r.get('success', False)])
            }
            
            # 4. 保存完整结果
            final_result_file = os.path.join(ocr_folder_path, "complete_ocr_result.json")
            with open(final_result_file, 'w', encoding='utf-8') as f:
                json.dump(final_result, f, ensure_ascii=False, indent=2)
            
            # 更新缓存映射（使用精简版数据以减少文件大小）
            ocr_mapping = self._load_ocr_mapping()
            lightweight_entry = self._create_lightweight_cache_entry(final_result)
            ocr_mapping[file_md5] = lightweight_entry
            self._save_ocr_mapping(ocr_mapping)

            
            log_with_timestamp(f"PDF OCR处理完成: {original_filename} - {total_pages}页")
            
            # 推送OCR完成事件
            if user_id:
                push_sse_event(user_id, 'ocr_complete', {
                    'filename': original_filename,
                    'total_pages': total_pages,
                    'success_pages': final_result['success_pages'],
                    'message': f'OCR转换完成！共处理 {total_pages} 页'
                })
            
            # 标记是否需要重新生成DOCX
            needs_docx_regenerate = extracted_new_images or ocr_called
            
            return {
                'success': True,
                'cached': False,
                'file_md5': file_md5,
                'result': final_result,
                'folder_path': ocr_folder_path,
                'docx_exists': False,
                'needs_docx_regenerate': needs_docx_regenerate
            }
            
        except Exception as e:
            error_msg = f"PDF OCR处理失败: {str(e)}"
            log_with_timestamp(error_msg)
            
            if user_id:
                push_sse_event(user_id, 'ocr_error', {
                    'filename': original_filename,
                    'error': error_msg,
                    'message': f'OCR转换失败: {error_msg}'
                })
            
            return {
                'success': False,
                'error': error_msg,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    def process_pdf_with_ocr_and_docx(self, pdf_path, original_filename="", generate_docx=True, force_regenerate=False, user_id=None, project_id=None):
        """
        使用OCR处理PDF文件并生成DOCX文件 - 增量处理版本
        
        特性：
        1. 只有在有新提取图片或新OCR请求时才重新生成DOCX
        2. 如果缓存完全有效且DOCX存在，直接返回
        
        Args:
            pdf_path: PDF文件路径
            original_filename: 原始文件名
            generate_docx: 是否生成DOCX文件（默认为True）
            force_regenerate: 是否强制重新生成（默认为False）
            user_id: 用户ID（用于SSE事件推送）
            project_id: 项目ID（用于更新后端状态存储）
            
        Returns:
            dict: 处理结果（包含OCR结果和DOCX生成信息）
        """
        # 首先执行标准OCR处理（包含增量机制）
        ocr_result = self.process_pdf_with_ocr(pdf_path, original_filename, force_regenerate, user_id, project_id=project_id)
        
        if not ocr_result['success']:
            return ocr_result

        # 校验 OCR 结果完整性
        if ocr_result.get('success'):
            res_data = ocr_result.get('result', {})
            total_p = res_data.get('total_pages', 0)
            current_p = len(res_data.get('page_results', []))
            
            if total_p > 0 and total_p != current_p:
                msg = f"OCR结果页数不匹配 (预期 {total_p} vs 实际 {current_p})"
                log_with_timestamp(f"⚠️ {msg}")
                
                if not force_regenerate:
                    log_with_timestamp("🔄 触发强制重新生成...")
                    return self.process_pdf_with_ocr_and_docx(
                        pdf_path, original_filename, generate_docx, 
                        force_regenerate=True, user_id=user_id, project_id=project_id
                    )
                else:
                    return {'success': False, 'error': msg}
        
        # 如果不需要生成DOCX，直接返回
        if not generate_docx:
            return ocr_result
        
        folder_path = ocr_result.get('folder_path', '')
        needs_docx_regenerate = ocr_result.get('needs_docx_regenerate', True)
        
        # 检查DOCX文件是否存在
        pdf_filename = os.path.basename(pdf_path)
        base_name = os.path.splitext(pdf_filename)[0]
        docx_path = os.path.join(folder_path, f"{base_name}_完整版.docx")
        docx_exists = os.path.exists(docx_path)
        
        # 决定是否需要生成DOCX
        if ocr_result.get('cached', False) and docx_exists and not needs_docx_regenerate:
            log_with_timestamp(f"DOCX文件已存在且无需更新，跳过生成: {original_filename}")
            return ocr_result
        
        # 需要生成或重新生成DOCX
        if needs_docx_regenerate or not docx_exists:
            log_with_timestamp(f"开始生成DOCX文件: {original_filename} (需要更新: {needs_docx_regenerate}, 文件存在: {docx_exists})")
            docx_info = self._generate_docx_files(folder_path, ocr_result['result'])
            
            # 将DOCX信息添加到结果中
            ocr_result['result']['docx_info'] = docx_info
            ocr_result['docx_exists'] = docx_info.get('docx_generated', False)
            
            # 更新最终结果文件
            final_result_file = os.path.join(folder_path, "complete_ocr_result.json")
            try:
                with open(final_result_file, 'w', encoding='utf-8') as f:
                    json.dump(ocr_result['result'], f, ensure_ascii=False, indent=2)
                log_with_timestamp(f"已更新完整OCR结果文件: {final_result_file}")
            except Exception as e:
                log_with_timestamp(f"更新完整结果文件失败: {e}")
        
        return ocr_result

    def _format_ocr_result(self, result, include_docx_info=False):
        """Common formatting of OCR result for convenience functions.

        Args:
            result (dict): The result dict returned by processing methods.
            include_docx_info (bool): Whether to include DOCX related fields.
        Returns:
            tuple: (extracted_text, processing_info)
        """
        if not result.get('success', False):
            return "", {'error': result.get('error', 'Unknown error')}
        final_result = result.get('result', {})
        extracted_text = final_result.get('combined_text', '')
        processing_info = {
            'total_pages': final_result.get('total_pages', 0),
            'success_pages': final_result.get('success_pages', 0),
            'failed_pages': final_result.get('failed_pages', 0),
            'cached': result.get('cached', False),
            'file_md5': final_result.get('file_md5', ''),
            'ocr_folder': final_result.get('ocr_folder', ''),
            'folder_path': result.get('folder_path', ''),
            'pdf_filename': final_result.get('pdf_filename', ''),
            'generation_time': final_result.get('extraction_time', ''),
            'combined_text': extracted_text,
        }
        if include_docx_info:
            processing_info.update({
                'docx_info': final_result.get('docx_info', {}),
                'docx_path': final_result.get('docx_info', {}).get('merged_file', ''),
                'docx_generated': final_result.get('docx_info', {}).get('docx_generated', False),
                'docx_exists': result.get('docx_exists', False),
                'regenerated_docx': result.get('regenerated_docx', False),
            })
        return extracted_text, processing_info

# 便捷函数
def process_image_pdf_ocr(pdf_path, original_filename="", force_regenerate=False, user_id=None):
    """
    便捷函数：处理图片PDF的OCR转换 - 新版文件夹结构
    
    Args:
        pdf_path: PDF文件路径
        original_filename: 原始文件名
        force_regenerate: 是否强制重新生成（默认为False）
        user_id: 用户ID（用于SSE事件推送）
        
    Returns:
        tuple: (extracted_text, processing_info)
    """
    processor = PDFOCRProcessor()
    result = processor.process_pdf_with_ocr(pdf_path, original_filename, force_regenerate, user_id)
    
    extracted_text, processing_info = processor._format_ocr_result(result, include_docx_info=False)
    return extracted_text, processing_info

def process_image_pdf_ocr_and_docx(pdf_path, original_filename="", generate_docx=True, force_regenerate=False, user_id=None, project_id=None, doc_type=None):
    """
    便捷函数：处理图片PDF的OCR转换并生成DOCX文件 - 新版文件夹结构
    
    Args:
        pdf_path: PDF文件路径
        original_filename: 原始文件名
        generate_docx: 是否生成DOCX文件（默认为True）
        force_regenerate: 是否强制重新生成（默认为False）
        user_id: 用户ID（用于SSE事件推送）
        project_id: 项目ID（用于更新后端状态存储）
        doc_type: 文档类型 (用于选择OCR模型)
        
    Returns:
        tuple: (extracted_text, processing_info)
    """
    processor = PDFOCRProcessor(save_ocr_txt=True, doc_type=doc_type)
    result = processor.process_pdf_with_ocr_and_docx(pdf_path, original_filename, generate_docx, force_regenerate, user_id, project_id=project_id)
    
    extracted_text, processing_info = processor._format_ocr_result(result, include_docx_info=True)
    return extracted_text, processing_info

def process_image_pdf_with_project_mapping(pdf_path, original_filename, project_id, file_md5, generate_docx=True, user_id=None):
    """
    处理图片PDF的OCR转换并更新项目映射 - 完整流程
    
    Args:
        pdf_path: PDF文件路径
        original_filename: 原始文件名
        project_id: 项目ID
        file_md5: PDF文件的MD5
        generate_docx: 是否生成DOCX文件（默认为True）
        user_id: 用户ID（必须提供，用于新路径结构）
        
    Returns:
        tuple: (extracted_text, processing_info)
    """
    from app.utils import log_with_timestamp
    
    try:
        log_with_timestamp(f"🔄 开始处理图片PDF并更新项目映射: {original_filename}")
        
        # 1. 执行OCR处理并生成DOCX
        processor = PDFOCRProcessor()
        result = processor.process_pdf_with_ocr_and_docx(
            pdf_path,
            original_filename,
            generate_docx=generate_docx,
            force_regenerate=False
        )
        
        if not result['success']:
            error_msg = result.get('error', 'OCR处理失败')
            log_with_timestamp(f"❌ OCR处理失败: {error_msg}")
            return "", {'error': error_msg}
        
        # 2. 提取OCR结果
        # 2. 提取OCR结果
        extracted_text, processing_info = processor._format_ocr_result(result, include_docx_info=True)
        
        docx_generated = processing_info.get('docx_generated', False)
        merged_docx_path = processing_info.get('docx_path')
        
        # 3. 如果生成了DOCX，更新项目映射
        if docx_generated and merged_docx_path and os.path.exists(merged_docx_path):
            log_with_timestamp(f"✅ DOCX已生成: {merged_docx_path}")
            
            try:
                # 导入必要的函数
                import hashlib
                from datetime import datetime
                
                # 计算DOCX文件的MD5
                with open(merged_docx_path, 'rb') as f:
                    docx_md5 = hashlib.md5(f.read()).hexdigest()
                
                docx_filename = os.path.basename(merged_docx_path)
                docx_size = os.path.getsize(merged_docx_path)
                
                log_with_timestamp(f"📝 DOCX文件信息: {docx_filename}, MD5: {docx_md5}, 大小: {docx_size}")
                
                # 更新MD5映射 - 添加DOCX文件到映射表
                from app.pipeline.when_upload_files.md5_manager import update_md5_entry
                
                # 添加DOCX到MD5映射
                update_md5_entry(docx_md5, {
                    'filename': docx_filename,
                    'upload_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'file_size': docx_size,
                    'converted_from': file_md5,  # 记录从哪个PDF转换来的
                    'conversion_type': 'ocr'
                })
                
                # 更新原PDF文件的映射 - 标记已转换
                update_md5_entry(file_md5, {
                    'converted_to': docx_md5,
                    'conversion_type': 'ocr',
                    'ocr_folder': result.get('folder_path', '')
                })
                
                log_with_timestamp(f"✅ MD5映射已更新: PDF({file_md5}) -> DOCX({docx_md5})")
                
                # Note: Project.json update has been removed as it was only used for contract analysis.
                # Cost-ai functionality does not require project file tracking.
                
                # 添加映射信息到返回结果
                processing_info['converted'] = True
                processing_info['docx_md5'] = docx_md5
                processing_info['docx_filename'] = docx_filename
                processing_info['project_updated'] = False  # No longer updating projects
                
            except Exception as map_error:
                log_with_timestamp(f"⚠️ 更新项目映射时出错: {map_error}")
                processing_info['mapping_error'] = str(map_error)
        else:
            log_with_timestamp(f"⚠️ DOCX未生成或文件不存在")
            processing_info['converted'] = False
        
        log_with_timestamp(f"✅ 图片PDF处理完成: {original_filename}")
        return extracted_text, processing_info
        
    except Exception as e:
        error_msg = f"处理图片PDF时出错: {str(e)}"
        log_with_timestamp(f"❌ {error_msg}")
        return "", {'error': error_msg}