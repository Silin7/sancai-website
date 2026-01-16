"""
文件页数统计工具
支持PDF和DOCX文件的页数读取
"""
import os
import fitz
from docx import Document
from ...utils import log_with_timestamp



def get_file_page_count(file_path, filename):
    """
    获取文件的页数
    
    Args:
        file_path: 文件路径
        filename: 文件名（用于判断类型）
    
    Returns:
        int: 页数，如果无法读取返回 None
    """
    if not os.path.exists(file_path):
        log_with_timestamp(f"文件不存在: {file_path}")
        return None
    
    file_ext = os.path.splitext(filename)[1].lower()
    
    try:
        if file_ext == '.pdf':
            return get_pdf_page_count(file_path)
        elif file_ext == '.docx':
            return get_docx_page_count(file_path)
        elif file_ext == '.doc':
            # DOC文件需要先转换为DOCX才能读取页数
            log_with_timestamp(f"DOC文件无法直接统计页数: {filename}")
            return None
        else:
            log_with_timestamp(f"不支持的文件格式: {file_ext}")
            return None
    except Exception as e:
        log_with_timestamp(f"读取文件页数失败 {filename}: {e}")
        return None


def get_pdf_page_count(file_path):
    """
    获取PDF文件的页数
    
    Args:
        file_path: PDF文件路径
    
    Returns:
        int: 页数
    """
    try:
        doc = fitz.open(file_path)
        page_count = len(doc)
        doc.close()
        return page_count
    except Exception as e:
        log_with_timestamp(f"读取PDF页数失败 {file_path}: {e}")
        return None


def get_docx_page_count(file_path):
    """
    获取DOCX文件的页数
    
    注意：python-docx 库本身不直接提供页数统计功能
    这里使用一个近似方法：通过段落数和表格数估算页数
    实际页数可能与Word显示的有差异
    
    Args:
        file_path: DOCX文件路径
    
    Returns:
        int: 估算的页数（如果无法估算返回None）
    """
    try:
        doc = Document(file_path)
        
        # 方法1: 尝试从文档属性中获取页数
        # 注意：这需要文档在保存时包含了统计信息
        try:
            core_props = doc.core_properties
            if hasattr(core_props, 'pages') and core_props.pages:
                return core_props.pages
        except:
            pass
        
        # 方法2: 粗略估算（每30个段落约1页，仅作为备选方案）
        # 这个估算非常粗糙，仅在无法获取准确页数时使用
        paragraph_count = len(doc.paragraphs)
        estimated_pages = max(1, paragraph_count // 30)
        
        log_with_timestamp(f"DOCX文件页数估算（可能不准确）: {estimated_pages}页")
        return estimated_pages
        
    except Exception as e:
        log_with_timestamp(f"读取DOCX页数失败 {file_path}: {e}")
        return None
