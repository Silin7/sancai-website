# app/data_storage/__init__.py
"""
数据存储模块 - 统一管理用户和文件元数据

包含:
- user_manager: 用户会话、头像、历史记录管理
- file_metadata: 文件MD5映射、任务进度
"""

# 从子模块导出常用函数
from .user_manager import (
    init_user_session,
    get_user_history,
    load_user_avatar,
    save_user_avatar,
    ensure_user_has_avatar,
    get_all_preset_avatars,
    load_metadata,
    save_metadata,
)

from .file_metadata import (
    load_md5_mapping,
    save_md5_mapping,
    update_md5_entry,
    get_file_by_md5,
    save_upload_file,
    convert_doc_file,
    # OCR status tracking
    set_file_ocr_status,
    get_file_ocr_status,
    get_project_ocr_status,
    clear_file_ocr_status,
)
