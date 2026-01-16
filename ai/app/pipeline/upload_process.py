# app/pipeline/upload_process.py
# 上传处理模块
# 重新导出 when_upload_files 中的相关函数以保持向后兼容性

from .when_upload_files.md5_manager import (
    load_md5_mapping,
    save_md5_mapping,
    update_md5_entry,
    get_file_by_md5,
)

from .when_upload_files.file_saver import (
    save_upload_file,
    convert_doc_file,
)