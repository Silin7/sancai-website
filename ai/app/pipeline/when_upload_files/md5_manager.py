# app/pipeline/upload/md5_manager.py
# MD5映射管理 - 从 project_file_manager.py 提取
# 负责文件MD5映射的加载、保存、更新和查询

import os
import json
import threading
from ...config import Config
from ...utils import log_with_timestamp

# 全局锁
_md5_lock = threading.Lock()

# ============ MD5映射 (uploads/file_md5_mapping.json) ============

def load_md5_mapping():
    """加载MD5映射"""
    if not os.path.exists(Config.FILE_MD5_MAPPING):
        return {}
    try:
        with open(Config.FILE_MD5_MAPPING, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_md5_mapping(data):
    """保存MD5映射"""
    os.makedirs(os.path.dirname(Config.FILE_MD5_MAPPING), exist_ok=True)
    with open(Config.FILE_MD5_MAPPING, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_md5_entry(md5_hash, info):
    """更新MD5条目"""
    with _md5_lock:
        mapping = load_md5_mapping()
        if md5_hash in mapping:
            mapping[md5_hash].update(info)
        else:
            mapping[md5_hash] = info
        save_md5_mapping(mapping)

def get_file_by_md5(md5_hash):
    """通过MD5获取文件"""
    with _md5_lock:
        mapping = load_md5_mapping()
        
        log_with_timestamp(f"🔍 get_file_by_md5 开始查找: MD5={md5_hash}")
        log_with_timestamp(f"📊 MD5映射文件存在: {os.path.exists(Config.FILE_MD5_MAPPING)}")
        log_with_timestamp(f"📊 映射记录数量: {len(mapping)}")
        
        if md5_hash in mapping:
            filename = mapping[md5_hash]['filename']
            file_info = mapping[md5_hash].copy()  # 复制信息避免修改原始数据
            path = os.path.join(Config.UPLOAD_FOLDER, filename)
            
            log_with_timestamp(f"✅ 找到MD5映射: {filename}, 路径: {path}")
            log_with_timestamp(f"📄 映射信息: {file_info}")
            
            try:
                if file_info.get('converted_from'):
                    # 🆕 检查转换类型，只有 PDF OCR 才需要 _OCR 子目录
                    conversion_type = file_info.get('conversion_type')
                    if conversion_type == 'pdf_ocr':
                        # PDF OCR 转换的文件存在 原始文件名_OCR/ 子目录中
                        original_info = mapping.get(file_info['converted_from'])
                        if original_info and original_info.get('filename'):
                            original_base = os.path.splitext(original_info['filename'])[0]
                            path = os.path.join(Config.UPLOAD_FOLDER, original_base + '_OCR', filename)
                            log_with_timestamp(f"🔄 OCR转换文件路径调整: {path}")
                    # DOC 转 DOCX 的文件直接在 uploads/ 根目录，无需调整路径
                    elif conversion_type == 'doc_to_docx':
                        log_with_timestamp(f"📄 DOC转DOCX文件，使用根目录路径: {path}")
            except Exception as e:
                log_with_timestamp(f"⚠️ 路径调整异常: {e}")
            
            if os.path.exists(path):
                log_with_timestamp(f"✅ 文件存在: {path}")
                
                # 如果没有原始大小信息，尝试从文件路径获取
                if not file_info.get('original_size') and file_info.get('converted_from'):
                    # 对于转换后的文件，尝试获取原始文件的大小信息
                    original_info = mapping.get(file_info['converted_from'])
                    if original_info and original_info.get('file_size'):
                        file_info['original_size'] = original_info['file_size']
                        log_with_timestamp(f"从原始文件获取大小: {file_info['original_size']} bytes")
                
                log_with_timestamp(f" get_file_by_md5 返回成功: {path}")
                return path, file_info
            else:
                log_with_timestamp(f"❌ 文件不存在: {path}")
        else:
            log_with_timestamp(f"❌ MD5未找到: {md5_hash}")
            # 显示所有MD5用于调试
            log_with_timestamp(f"🔍 可用的MD5列表: {list(mapping.keys())[:10]}")  # 只显示前10个
    
    log_with_timestamp(f"❌ get_file_by_md5 返回失败: {md5_hash}")
    return None, None
