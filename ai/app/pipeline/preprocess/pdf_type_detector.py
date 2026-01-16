# app/pipeline/preprocess/pdf_type_detector.py
# PDF类型检测工具 - 判断PDF是否为图片型PDF

import fitz  # PyMuPDF
from ...utils import log_with_timestamp

# 判断阈值配置
MIN_TOTAL_CHARS = 50              # 最小总字符数阈值
MIN_AVG_CHARS_PER_PAGE = 20       # 最小平均每页字符数阈值
MIN_TEXT_COVERAGE = 0.3           # 最小文字页面覆盖率 (30%)
MIN_IMAGE_COVERAGE = 0.5          # 图像页面覆盖率阈值 (50%)


def is_image_based_pdf(pdf_path: str) -> dict:
    """
    判断PDF是否为图片型PDF
    
    通过综合分析文字内容和图像信息来判断PDF类型，比简单的"无文字即图片型"更加准确。
    
    Args:
        pdf_path: PDF文件路径
        
    Returns:
        dict: 判断结果，包含以下字段：
            - is_image_pdf (bool): 是否为图片型PDF
            - confidence (float): 判断置信度 (0-1)
            - total_pages (int): 总页数
            - text_char_count (int): 总文字字符数
            - avg_chars_per_page (float): 平均每页字符数
            - pages_with_text (int): 有文字的页面数
            - text_coverage (float): 文字覆盖率 (0-1)
            - has_images (bool): 是否包含图像
            - image_pages (int): 包含图像的页面数
            - image_coverage (float): 图像页面覆盖率 (0-1)
            - reason (str): 判断理由
    """
    try:
        # 提取文字统计信息
        text_stats = extract_pdf_text_stats(pdf_path)
        
        # 检测图像信息
        image_stats = detect_pdf_images(pdf_path)
        
        # 综合判断
        total_pages = text_stats['total_pages']
        text_char_count = text_stats['text_char_count']
        avg_chars_per_page = text_stats['avg_chars_per_page']
        pages_with_text = text_stats['pages_with_text']
        text_coverage = text_stats['text_coverage']
        
        has_images = image_stats['has_images']
        image_pages = image_stats['image_pages']
        image_coverage = image_stats['image_coverage']
        
        # 判断逻辑
        is_image_pdf = False
        reason = ""
        confidence = 0.0
        
        # 规则1: 总字符数极少且有图像 → 图片型PDF
        if text_char_count < MIN_TOTAL_CHARS and has_images:
            is_image_pdf = True
            reason = f"总字符数仅 {text_char_count} 个（< {MIN_TOTAL_CHARS}），且包含图像"
            confidence = 0.95
        
        # 规则2: 平均每页字符数极少 → 图片型PDF
        elif avg_chars_per_page < MIN_AVG_CHARS_PER_PAGE:
            is_image_pdf = True
            reason = f"平均每页仅 {avg_chars_per_page:.1f} 个字符（< {MIN_AVG_CHARS_PER_PAGE}）"
            confidence = 0.90
        
        # 规则3: 文字覆盖率低 + 图像覆盖率高 → 图片型PDF
        elif text_coverage < MIN_TEXT_COVERAGE and image_coverage > MIN_IMAGE_COVERAGE:
            is_image_pdf = True
            reason = f"文字页面占比 {text_coverage:.1%}（< {MIN_TEXT_COVERAGE:.0%}），图像页面占比 {image_coverage:.1%}（> {MIN_IMAGE_COVERAGE:.0%}）"
            confidence = 0.85
        
        # 规则4: 完全无文字 → 图片型PDF
        elif text_char_count == 0:
            is_image_pdf = True
            reason = "PDF中无任何可提取文字"
            confidence = 1.0 if has_images else 0.8  # 有图像时置信度更高
        
        # 否则判定为文字型PDF
        else:
            is_image_pdf = False
            reason = f"文字充足（总字符数: {text_char_count}, 平均每页: {avg_chars_per_page:.1f}）"
            # 计算文字型的置信度
            confidence = min(1.0, (avg_chars_per_page / 100) * 0.5 + text_coverage * 0.5)
        
        # 构建返回结果
        result = {
            'is_image_pdf': is_image_pdf,
            'confidence': confidence,
            'total_pages': total_pages,
            'text_char_count': text_char_count,
            'avg_chars_per_page': avg_chars_per_page,
            'pages_with_text': pages_with_text,
            'text_coverage': text_coverage,
            'has_images': has_images,
            'image_pages': image_pages,
            'image_coverage': image_coverage,
            'reason': reason
        }
        
        # 输出判断日志
        if is_image_pdf:
            log_with_timestamp(
                f"PDF类型检测完成: {pdf_path}\n"
                f"  - 判断结果: {'图片型PDF' if is_image_pdf else '文字型PDF'}\n"
                f"  - 置信度: {confidence:.2%}\n"
                f"  - 总页数: {total_pages}\n"
                f"  - 总字符数: {text_char_count}\n"
                f"  - 平均每页字符数: {avg_chars_per_page:.1f}\n"
                f"  - 文字页面占比: {text_coverage:.1%}\n"
                f"  - 图像页面占比: {image_coverage:.1%}\n"
                f"  - 判断理由: {reason}"
            )
        
        return result
        
    except Exception as e:
        log_with_timestamp(f"PDF类型检测失败 {pdf_path}: {e}")
        # 发生异常时，返回保守的判断结果
        return {
            'is_image_pdf': False,  # 保守判断为文字型，避免不必要的OCR
            'confidence': 0.0,
            'total_pages': 0,
            'text_char_count': 0,
            'avg_chars_per_page': 0.0,
            'pages_with_text': 0,
            'text_coverage': 0.0,
            'has_images': False,
            'image_pages': 0,
            'image_coverage': 0.0,
            'reason': f'检测失败: {str(e)}'
        }


def extract_pdf_text_stats(pdf_path: str) -> dict:
    """
    提取PDF的文字统计信息
    
    Args:
        pdf_path: PDF文件路径
        
    Returns:
        dict: 文字统计信息
            - total_pages (int): 总页数
            - text_char_count (int): 总文字字符数（去除空白字符）
            - avg_chars_per_page (float): 平均每页字符数
            - pages_with_text (int): 有文字的页面数
            - text_coverage (float): 文字覆盖率 (有文字的页面数 / 总页数)
    """
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    total_chars = 0
    pages_with_text = 0
    
    for page in doc:
        text = page.get_text()
        char_count = len(text.strip())
        total_chars += char_count
        
        if char_count > 0:
            pages_with_text += 1
    
    doc.close()
    
    avg_chars_per_page = total_chars / total_pages if total_pages > 0 else 0.0
    text_coverage = pages_with_text / total_pages if total_pages > 0 else 0.0
    
    return {
        'total_pages': total_pages,
        'text_char_count': total_chars,
        'avg_chars_per_page': avg_chars_per_page,
        'pages_with_text': pages_with_text,
        'text_coverage': text_coverage
    }


def detect_pdf_images(pdf_path: str) -> dict:
    """
    检测PDF中的图像信息
    
    Args:
        pdf_path: PDF文件路径
        
    Returns:
        dict: 图像统计信息
            - has_images (bool): 是否包含图像
            - image_pages (int): 包含图像的页面数
            - total_images (int): 图像总数
            - image_coverage (float): 图像页面覆盖率 (包含图像的页面数 / 总页数)
    """
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    image_pages = 0
    total_images = 0
    
    for page in doc:
        images = page.get_images(full=False)
        if images:
            image_pages += 1
            total_images += len(images)
    
    doc.close()
    
    has_images = total_images > 0
    image_coverage = image_pages / total_pages if total_pages > 0 else 0.0
    
    return {
        'has_images': has_images,
        'image_pages': image_pages,
        'total_images': total_images,
        'image_coverage': image_coverage
    }
