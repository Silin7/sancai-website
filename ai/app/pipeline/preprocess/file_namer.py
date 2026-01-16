# app/pipeline/preprocess/file_namer.py
# 文件命名工具
import os
import uuid
from datetime import datetime
from ...utils import log_with_timestamp


def get_unique_filename(folder, filename, use_space=True):
    """
    在指定文件夹中生成一个唯一的文件名。
    如果文件名已存在，则在其末尾附加时间戳。
    
    参数:
        folder: 目标文件夹
        filename: 原始文件名
        use_space: True=使用空格格式 "basename yyyymmdd hh-mm-ss.ext"
                   False=使用下划线格式 "basename_yyyymmdd_hhmmss.ext"（向后兼容）
    """
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        return filename

    basename, extension = os.path.splitext(filename)
    
    if use_space:
        # ✅ 新格式：空格 + yyyymmdd hh-mm-ss
        timestamp = datetime.now().strftime('%Y%m%d %H-%M-%S')
        new_filename = f"{basename} {timestamp}{extension}"
    else:
        # 旧格式：下划线 + yyyymmdd_hhmmss
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        new_filename = f"{basename}_{timestamp}{extension}"

    # 确保文件名唯一
    counter = 1
    while os.path.exists(os.path.join(folder, new_filename)):
        if use_space:
            new_filename = f"{basename} {timestamp}-{counter}{extension}"
        else:
            new_filename = f"{basename}_{timestamp}_{counter}{extension}"
        counter += 1

    return new_filename

def generate_contract_id():
    """生成唯一的合同ID"""
    return str(uuid.uuid4())[:8]

def generate_result_filename(contract_id, original_filename):
    """生成分析结果文件名"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"contract_{timestamp}_{contract_id}.json"