# app/pipeline/preprocess/file_validator.py
# 文件校验和MD5工具
import os
import hashlib
from ...config import Config
from ...utils import log_with_timestamp


def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def calculate_md5(file_storage):
    """计算werkzeug FileStorage对象的MD5值"""
    hash_md5 = hashlib.md5()
    # 移动文件指针到开头
    file_storage.seek(0)
    # 分块读取以处理大文件
    for chunk in iter(lambda: file_storage.read(4096), b""):
        hash_md5.update(chunk)
    # 读取后将文件指针移回开头，以便后续保存
    file_storage.seek(0)
    return hash_md5.hexdigest()

def validate_file_integrity(file_path, expected_md5=None):
    """验证文件完整性"""
    if not os.path.exists(file_path):
        return False, "文件不存在"

    if expected_md5:
        with open(file_path, 'rb') as f:
            actual_md5 = hashlib.md5(f.read()).hexdigest()
        if actual_md5 != expected_md5:
            return False, f"MD5校验失败，期望: {expected_md5}, 实际: {actual_md5}"

    return True, "文件校验通过"