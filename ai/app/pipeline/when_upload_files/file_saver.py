# app/pipeline/upload/file_saver.py
# 负责文件上传保存、DOC转DOCX转换

import os
import hashlib
from datetime import datetime
from ...config import Config
from ...utils import log_with_timestamp
from ..preprocess.file_namer import get_unique_filename
from ..preprocess.file_parser import convert_doc_to_docx,convert_doc_to_pdf
from ..preprocess.file_validator import calculate_md5
from .md5_manager import get_file_by_md5, update_md5_entry


# ============ 文件保存 (uploads/) ============

def save_upload_file(file_storage, original_name):
    """保存文件到uploads并返回MD5"""
    md5 = calculate_md5(file_storage)
    
    # 检查复用
    existing_path, existing_info = get_file_by_md5(md5)
    if existing_path:
        log_with_timestamp(f"文件复用 MD5={md5}: {existing_info['filename']}")
        return existing_path, existing_info['filename'], md5
    
    # 生成文件名
    filename = get_unique_filename(Config.UPLOAD_FOLDER, original_name, use_space=True)
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    
    file_storage.save(file_path)
    
    # 更新映射
    update_md5_entry(md5, {
        'filename': filename,
        'upload_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'file_size': os.path.getsize(file_path)
    })
    
    log_with_timestamp(f"文件已保存: {filename} (MD5: {md5})")
    return file_path, filename, md5

def convert_doc_file(doc_path, doc_md5, original_name):
    """
    DOC转换（根据开关生成 PDF 或 DOCX）
    
    内部开关 USE_PDF_OUTPUT 控制生成哪种格式：
    - True: 生成 PDF（默认，用于后续 fitz 解析）
    - False: 生成 DOCX（用于后续 python-docx 解析）
    """
    # ========== 内部开关：True=生成PDF, False=生成DOCX ==========
    USE_PDF_OUTPUT = True
    # ===========================================================
    
    # 清理文件名
    clean_name = original_name.replace('\n', '').replace('\r', '')
    clean_name = ' '.join(clean_name.split())
    base = os.path.splitext(clean_name)[0]
    
    if USE_PDF_OUTPUT:
        # ========== 生成 PDF ==========
        temp_file = convert_doc_to_pdf(doc_path)
        
        with open(temp_file, 'rb') as f:
            file_md5_value = hashlib.md5(f.read()).hexdigest()
        
        file_name = f"{base}.pdf"
        file_name = get_unique_filename(Config.UPLOAD_FOLDER, file_name, use_space=True)
        final_path = os.path.join(Config.UPLOAD_FOLDER, file_name)
        os.rename(temp_file, final_path)
        
        log_with_timestamp(f"DOC→PDF: {os.path.basename(doc_path)} → {file_name}")
    else:
        # ========== 生成 DOCX ==========
        temp_file = convert_doc_to_docx(doc_path)
        
        with open(temp_file, 'rb') as f:
            file_md5_value = hashlib.md5(f.read()).hexdigest()
        
        file_name = f"{base}.docx"
        file_name = get_unique_filename(Config.UPLOAD_FOLDER, file_name, use_space=True)
        final_path = os.path.join(Config.UPLOAD_FOLDER, file_name)
        os.rename(temp_file, final_path)
        
        log_with_timestamp(f"DOC→DOCX: {os.path.basename(doc_path)} → {file_name}")
    
    # 更新 MD5 映射
    update_md5_entry(doc_md5, {'converted_to': file_md5_value})
    update_md5_entry(file_md5_value, {
        'filename': file_name,
        'upload_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'file_size': os.path.getsize(final_path),
        'converted_from': doc_md5
    })
    
    return final_path, file_md5_value, file_name
