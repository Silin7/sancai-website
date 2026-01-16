import os
import cv2
import numpy as np
import pickle
from ...utils import log_with_timestamp

# ========== 配置开关 ==========
USE_PADDLE_OCR = True  # True: 使用 PaddleOCR，False: 使用 LR 模型
CONFIDENCE_THRESHOLD = 0.6  # 置信度阈值
SAVE_AI_DEBUG_IMAGE = True  # True: 保存发送给 AI 的图片到调试目录

# 跳过 PaddleOCR 模型源连接检查（加速启动）
os.environ["DISABLE_MODEL_SOURCE_CHECK"] = "True"


class PaddleOrientationDetector:
    """
    使用 PaddleOCR 的页面方向检测器
    支持检测 0°, 90°, 180°, 270° 四个方向
    """
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaddleOrientationDetector, cls).__new__(cls)
            cls._instance._load_model()
        return cls._instance
    
    def _load_model(self):
        try:
            # 跳过模型源连接检查（加速启动）
            import os
            os.environ["DISABLE_MODEL_SOURCE_CHECK"] = "True"
            
            from paddleocr import DocImgOrientationClassification
            log_with_timestamp("  [Orientation] 正在加载 PaddleOCR...")
            self._model = DocImgOrientationClassification(model_name="PP-LCNet_x1_0_doc_ori")
            log_with_timestamp("  [Orientation] 方向分类模型加载成功")
        except ImportError as e:
            log_with_timestamp(f"  [Orientation] WARN: paddleocr 导入失败: {e}")
            log_with_timestamp("  [Orientation] 请运行: pip install paddleocr paddleclas paddlepaddle")
            self._model = None
        except Exception as e:
            import traceback
            log_with_timestamp(f"  [Orientation] PaddleOCR 模型加载失败: {type(e).__name__}: {e}")
            log_with_timestamp(f"  [Orientation] 详细错误:\n{traceback.format_exc()}")
            self._model = None
    
    def detect_orientation(self, img_cv):
        """
        检测方向
        Args:
            img_cv: OpenCV 图像 (BGR) 或图片路径
        Returns:
            int: 0 (0°), 1 (90°), 2 (180°), 3 (270°)
            float: 置信度
        """
        if self._model is None:
            return 0, 0.0
        
        try:
            # PaddleOCR 支持直接传入 numpy array
            # 但需要转换为 RGB
            if isinstance(img_cv, np.ndarray):
                img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
            else:
                img_rgb = img_cv
            
            results = self._model.predict(img_rgb)
            
            for res in results:
                label = res["label_names"][0]  # e.g., "0_degree", "180_degree"
                score = float(res["scores"][0])
                
                # 解析角度
                if "180" in label:
                    return 2, score  # 180°
                elif "90" in label:
                    return 1, score  # 90°
                elif "270" in label:
                    return 3, score  # 270°
                else:
                    return 0, score  # 0°
            
            return 0, 0.0
            
        except Exception as e:
            log_with_timestamp(f"  [Orientation] PaddleOCR 预测异常: {e}")
            return 0, 0.0
    
    def process_image(self, img_cv, debug_dir=None, image_name=None):
        """
        处理图像：如果检测到非正向，则旋转
        Args:
            img_cv: BGR image
            debug_dir: 可选的调试目录路径（用于保存 AI 判断的图片）
            image_name: 原始图片名称（不含扩展名），用于命名调试图片
        Returns:
            tuple: (processed_img, is_rotated, debug_info)
        """
        pred, conf = self.detect_orientation(img_cv)
        
        if conf < CONFIDENCE_THRESHOLD:
            log_with_timestamp(f"  [Orientation] Paddle 置信度低 ({conf:.2f} < {CONFIDENCE_THRESHOLD}) -> 尝试预处理后重新检测")
            
            # 第二次尝试：使用预处理后的图像
            img_enhanced = self._enhance_sparse_text(img_cv)
            img_processed = self._crop_text_regions(img_enhanced)
            
            # 保存预处理后的图片
            if SAVE_AI_DEBUG_IMAGE and debug_dir and image_name:
                preprocess_dir = os.path.join(debug_dir, 'orientation_debug')
                os.makedirs(preprocess_dir, exist_ok=True)
                preprocess_path = os.path.join(preprocess_dir, f"{image_name}_preprocessed.png")
                cv2.imwrite(preprocess_path, img_processed)
                log_with_timestamp(f"  [Orientation] 预处理图片已保存: {preprocess_path}")
            
            pred2, conf2 = self.detect_orientation(img_processed)
            
            if conf2 >= CONFIDENCE_THRESHOLD:
                log_with_timestamp(f"  [Orientation] 预处理后 Paddle 置信度提升: {conf:.2f} -> {conf2:.2f}")
                # 使用预处理后的结果
                pred, conf = pred2, conf2
            else:
                log_with_timestamp(f"  [Orientation] 预处理后置信度仍低 ({conf2:.2f}) -> 调用 AI 判断")
                # 调用 AI Fallback
                ai_result = self._ask_ai_for_orientation(img_cv, debug_dir, image_name)
                if ai_result == "inverted":
                    log_with_timestamp(f"  [Orientation] AI 判断: 倒置 -> 执行 180° 旋转")
                    rotated = cv2.rotate(img_cv, cv2.ROTATE_180)
                    return rotated, True, f"AI判断倒置 (Paddle conf: {conf:.2f}/{conf2:.2f})"
                else:
                    log_with_timestamp(f"  [Orientation] AI 判断: 正常 -> 保持原样")
                    return img_cv, False, f"AI判断正常 (Paddle conf: {conf:.2f}/{conf2:.2f})"
        
        if pred == 2:  # 180°
            log_with_timestamp(f"  [Orientation] 检测到倒置 180° (置信度 {conf:.2f}) -> 执行旋转")
            rotated = cv2.rotate(img_cv, cv2.ROTATE_180)
            return rotated, True, f"Inverted 180° (conf: {conf:.2f})"
        elif pred == 1:  # 90°
            log_with_timestamp(f"  [Orientation] 检测到 90° 旋转 (置信度 {conf:.2f}) -> 执行逆时针旋转 90°")
            rotated = cv2.rotate(img_cv, cv2.ROTATE_90_COUNTERCLOCKWISE)
            return rotated, True, f"Rotated 90° (conf: {conf:.2f})"
        elif pred == 3:  # 270°
            log_with_timestamp(f"  [Orientation] 检测到 270° 旋转 (置信度 {conf:.2f}) -> 执行顺时针旋转 90°")
            rotated = cv2.rotate(img_cv, cv2.ROTATE_90_CLOCKWISE)
            return rotated, True, f"Rotated 270° (conf: {conf:.2f})"
        else:
            log_with_timestamp(f"  [Orientation] 方向正常 (置信度 {conf:.2f})")
            return img_cv, False, f"Normal (conf: {conf:.2f})"
    
    def _enhance_sparse_text(self, img_cv):
        """
        增强稀疏文字对比度，让文字更明显
        使用 CLAHE（对比度受限的自适应直方图均衡化）
        """
        try:
            gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            enhanced = clahe.apply(gray)
            return cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            log_with_timestamp(f"  [Orientation] 图像增强失败: {e}")
            return img_cv
    
    def _crop_text_regions(self, img_cv):
        """
        裁剪出有文字的区域，去除大片空白
        保留足够边距以提供上下文（特别是页码位置）
        """
        try:
            gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
            
            # 使用 Otsu 自适应阈值，更好地处理不同对比度的图像
            _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            
            # 形态学操作：膨胀以连接相邻文字，闭运算去除小噪点
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
            binary = cv2.dilate(binary, kernel, iterations=2)
            
            coords = cv2.findNonZero(binary)
            
            if coords is not None:
                x, y, w, h = cv2.boundingRect(coords)
                
                # 使用更大的边距，确保页码等边缘元素被保留
                margin_x = max(100, int(img_cv.shape[1] * 0.05))  # 至少100像素或5%宽度
                margin_y = max(150, int(img_cv.shape[0] * 0.1))   # 至少150像素或10%高度
                
                x = max(0, x - margin_x)
                y = max(0, y - margin_y)
                w = min(img_cv.shape[1] - x, w + 2 * margin_x)
                h = min(img_cv.shape[0] - y, h + 2 * margin_y)
                
                cropped = img_cv[y:y+h, x:x+w]
                
                # 确保裁剪后的图像足够大（至少200x200）
                if cropped.shape[0] >= 200 and cropped.shape[1] >= 200:
                    log_with_timestamp(f"  [Orientation] 裁剪区域: ({x}, {y}) -> ({x+w}, {y+h})")
                    return cropped
            
            log_with_timestamp(f"  [Orientation] 未检测到有效文字区域，保持原图")
            return img_cv
        except Exception as e:
            log_with_timestamp(f"  [Orientation] 图像裁剪失败: {e}")
            return img_cv

    def _ask_ai_for_orientation(self, img_cv, debug_dir=None, image_name=None):
        """
        调用 AI 判断图片方向
        使用 DashScopeOCRClient.call_vl_chat，复用重试策略
        
        Args:
            img_cv: BGR image
            debug_dir: 可选的调试目录路径
            image_name: 原始图片名称（不含扩展名）
        Returns:
            str: "normal" 或 "inverted"
        """
        import tempfile
        import json
        
        try:
            from .ocr_api_client import DashScopeOCRClient
            
            # 图像预处理：增强对比度 + 裁剪文字区域
            log_with_timestamp(f"  [Orientation] 对图像进行预处理（增强对比度、裁剪文字区域）...")
            img_enhanced = self._enhance_sparse_text(img_cv)
            img_processed = self._crop_text_regions(img_enhanced)
            
            # 保存预处理后的图片使用PNG格式(无损)
            _, buffer = cv2.imencode('.png', img_processed)

            import tempfile
            
            # 确定调试目录：优先使用传入的 debug_dir
            if SAVE_AI_DEBUG_IMAGE and debug_dir:
                # 使用传入的 images 目录下的 orientation_debug 子目录
                actual_debug_dir = os.path.join(debug_dir, 'orientation_debug')
                os.makedirs(actual_debug_dir, exist_ok=True)
                # 使用原始图片名而非时间戳
                base_name = image_name if image_name else 'unknown'
                debug_filename = f"{base_name}_ai_check.png"
                tmp_path = os.path.join(actual_debug_dir, debug_filename)
                with open(tmp_path, 'wb') as f:
                    f.write(buffer.tobytes())
                log_with_timestamp(f"  [Orientation] AI 调试图片已保存: {tmp_path} ({len(buffer)} bytes)")
            else:
                # 使用临时文件
                with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp_file:
                    tmp_path = tmp_file.name
                    tmp_file.write(buffer.tobytes())
            
            try:
                prompt = """Analyze the orientation of text in this image.

CRITICAL: Look at these specific features:
1. Chinese characters stroke direction (top strokes vs bottom strokes)
2. Parentheses direction: ( ) vs ) (
3. Numbers orientation: are they upside down?

Return ONLY this JSON format:
{"orientation": "normal"} - if text reads normally top-to-bottom
{"orientation": "inverted"} - if image needs 180° rotation to read properly

Look carefully at punctuation marks like periods (。) and commas (,) - their position relative to characters is a strong indicator.
"""
                
                # 使用 DashScopeOCRClient 调用 VL 模型
                ocr_client = DashScopeOCRClient()
                content = ocr_client.call_vl_chat(tmp_path, prompt, max_retries=2)
                
                log_with_timestamp(f"  [Orientation] AI 返回: {content}")
                
                # 解析 JSON 响应
                try:
                    # 清理可能的 markdown 代码块
                    if "```" in content:
                        content = content.split("```")[1]
                        if content.startswith("json"):
                            content = content[4:]
                    
                    data = json.loads(content.strip())
                    orientation = data.get("orientation", "normal")
                    return orientation
                except json.JSONDecodeError:
                    # 简单文本匹配
                    if "inverted" in content.lower() or "倒" in content:
                        return "inverted"
                    return "normal"
                    
            finally:
                # 不再删除调试图片，保留在缓存目录供调试
                pass
                    
        except Exception as e:
            log_with_timestamp(f"  [Orientation] AI 调用失败: {e}, 默认返回 normal")
            return "normal"


class LROrientationDetector:
    """
    页面方向检测器 (原 OrientationDetector)
    使用轻量级机器学习模型 (Logistic Regression) 判断页面是否倒置 (180度)
    """
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LROrientationDetector, cls).__new__(cls)
            cls._instance._load_model()
        return cls._instance
    
    def _load_model(self):
        try:
            # 先尝试项目根目录
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
            model_path_root = os.path.join(base_dir, 'orientation_model.pkl')
            
            # 如果根目录没有，再尝试 assets 目录
            if not os.path.exists(model_path_root):
                current_dir = os.path.dirname(os.path.abspath(__file__))
                model_path = os.path.join(current_dir, 'assets', 'orientation_model.pkl')
            else:
                model_path = model_path_root
            
            if os.path.exists(model_path):
                with open(model_path, 'rb') as f:
                    self._model = pickle.load(f)
                log_with_timestamp(f"  [Orientation] LR 模型加载成功: {model_path}")
            else:
                log_with_timestamp(f"  [Orientation] WARN: LR 模型未找到: {model_path}")
                self._model = None
        except Exception as e:
            log_with_timestamp(f"  [Orientation] LR 模型加载失败: {e}")
            self._model = None

    def _extract_features(self, img_gray):
        """
        提取特征: 64x64 Thumbnail + Vertical Profile + Horizontal Profile
        必须与训练时完全一致
        """
        try:
            # 1. Resize to 64x64
            thumb_size = (64, 64)
            thumb = cv2.resize(img_gray, thumb_size)
            
            # Invert so text is high value (255)
            thumb_inv = 255 - thumb
            
            # Flatten Thumbnail (4096)
            thumb_feat = thumb_inv.flatten() / 255.0
            
            # Cast to float
            thumb_float = thumb_inv.astype(float)
            
            # Vertical Profile (Row sums) - Captures Header/Footer location
            row_profile = np.sum(thumb_float, axis=1)
            row_profile = row_profile / (np.max(row_profile) + 1e-5)
            
            # Horizontal Profile (Col sums) - Captures Columns/Margins
            col_profile = np.sum(thumb_float, axis=0)
            col_profile = col_profile / (np.max(col_profile) + 1e-5)
            
            # Combine
            return np.concatenate([thumb_feat, row_profile, col_profile])
            
        except Exception as e:
            log_with_timestamp(f"  [Orientation] 特征提取失败: {e}")
            return None

    def detect_orientation(self, img_cv):
        """
        检测方向
        Returns:
            int: 0 (Normal), 1 (Inverted 180)
            float: Confidence associated with the prediction
        """
        if self._model is None or img_cv is None:
            return 0, 0.0
            
        try:
            if len(img_cv.shape) == 3:
                gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
            else:
                gray = img_cv
                
            features = self._extract_features(gray)
            if features is None:
                return 0, 0.0
                
            # Predict
            pred = self._model.predict([features])[0]
            probs = self._model.predict_proba([features])[0]
            confidence = probs[pred]
            
            return pred, confidence
            
        except Exception as e:
            log_with_timestamp(f"  [Orientation] 预测异常: {e}")
            return 0, 0.0

    def process_image(self, img_cv, debug_dir=None):
        """
        处理图像：如果检测到倒置，则旋转
        Args:
            img_cv: BGR image
            debug_dir: 可选的调试目录路径（LR 模型不使用，保留接口一致）
        Returns:
            tuple: (processed_img, is_rotated, debug_info)
        """
        pred, conf = self.detect_orientation(img_cv)
        
        if pred == 1 and conf > CONFIDENCE_THRESHOLD:
            log_with_timestamp(f"  [Orientation] 检测到倒置 (置信度 {conf:.2f}) -> 执行 180° 旋转")
            rotated = cv2.rotate(img_cv, cv2.ROTATE_180)
            return rotated, True, f"Inverted (conf: {conf:.2f})"
        else:
            return img_cv, False, f"Normal (conf: {conf:.2f})"


class OrientationDetector:
    """
    统一方向检测入口
    根据 USE_PADDLE_OCR 配置选择检测引擎
    """
    _instance = None
    _detector = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrientationDetector, cls).__new__(cls)
            cls._instance._init_detector()
        return cls._instance
    
    def _init_detector(self):
        if USE_PADDLE_OCR:
            log_with_timestamp("  [Orientation] 使用 PaddleOCR 引擎")
            self._detector = PaddleOrientationDetector()
        else:
            log_with_timestamp("  [Orientation] 使用 LR 模型引擎")
            self._detector = LROrientationDetector()
    
    def detect_orientation(self, img_cv):
        """
        检测方向
        Returns:
            int: 方向标识
            float: 置信度
        """
        return self._detector.detect_orientation(img_cv)
    
    def process_image(self, img_cv, debug_dir=None, image_name=None):
        """
        处理图像：如果检测到非正向，则旋转
        Args:
            img_cv: BGR image
            debug_dir: 可选的调试目录路径
            image_name: 原始图片名称（不含扩展名）
        Returns:
            tuple: (processed_img, is_rotated, debug_info)
        """
        return self._detector.process_image(img_cv, debug_dir, image_name)
