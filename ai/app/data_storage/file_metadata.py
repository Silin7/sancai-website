# app/data_storage/file_metadata.py
"""File metadata and progress management module.

This module consolidates task progress caching and project status utilities.
MD5 mapping and file upload handling are now provided by `app.pipeline.upload`.
This module re-exports those functions for backward compatibility.
"""

import os
import json
import threading
from datetime import datetime
from ..config import Config
from ..utils import log_with_timestamp

# ==================== Re-export from pipeline.upload ====================
# 这些函数现在由 pipeline.upload 模块提供
# 为了向后兼容，从这里重新导出
from ..pipeline.upload_process import (
    load_md5_mapping,
    save_md5_mapping,
    update_md5_entry,
    get_file_by_md5,
    save_upload_file,
    convert_doc_file,
)


# ==================== Task Progress ====================
_task_progress = {}
_task_progress_lock = threading.Lock()

def update_task_progress(user_id, project_id, task_name, progress_data):
    """Cache real‑time task progress for UI refreshes.
    ``progress_data`` should contain keys like ``status``, ``progress`` etc.
    """
    with _task_progress_lock:
        key = (user_id, project_id, task_name)
        _task_progress.setdefault(key, {}).update(progress_data)
        _task_progress[key]["last_updated"] = datetime.now().strftime(  "%Y-%m-%d %H:%M:%S"     )
        #log_with_timestamp( f"🔄 Update task cache: {task_name} - {_task_progress[key].get('status')}"    )

def get_task_progress(user_id, project_id, task_name):
    """Retrieve cached progress for a single task.
    Returns ``None`` if no entry exists.
    """
    with _task_progress_lock:
        return _task_progress.get((user_id, project_id, task_name))

def get_project_all_tasks_progress(user_id, project_id):
    """Return a dict of all cached tasks for a project.
    ``{task_name: progress_dict}``
    """
    with _task_progress_lock:
        result = {}
        for (uid, pid, tname), prog in _task_progress.items():
            if uid == user_id and pid == project_id:
                result[tname] = prog
        return result

def clear_project_task_progress(user_id, project_id):
    """Remove all cached task entries for a project.
    Used when a project is completed or aborted.
    """
    with _task_progress_lock:
        keys = [k for k in _task_progress if k[0] == user_id and k[1] == project_id]
        for k in keys:
            del _task_progress[k]
        if keys:
            log_with_timestamp(
                f"🗑️ Cleared {len(keys)} task caches for project {project_id}"
            )

# ==================== OCR Progress Tracking ====================
# Track OCR processing status for files (survives page refresh within same server session)
_file_ocr_status = {}  # {(user_id, project_id, file_md5): {'status': 'converting', 'progress': 50, ...}}
_ocr_status_lock = threading.Lock()

# 🆕 OCR Cancellation Flags
_ocr_cancellation_flags = set()  # set of (user_id, project_id, file_md5)
_cancellation_lock = threading.Lock()

def set_ocr_cancellation(user_id, project_id, file_md5):
    """Set cancellation flag for a specific file OCR process."""
    with _cancellation_lock:
        key = (user_id, project_id, file_md5)
        _ocr_cancellation_flags.add(key)
        log_with_timestamp(f"🛑 OCR cancellation requested for: {key}")

def check_ocr_cancellation(user_id, project_id, file_md5):
    """Check if cancellation has been requested for this file."""
    with _cancellation_lock:
        key = (user_id, project_id, file_md5)
        return key in _ocr_cancellation_flags

def clear_ocr_cancellation(user_id, project_id, file_md5):
    """Clear cancellation flag."""
    with _cancellation_lock:
        key = (user_id, project_id, file_md5)
        if key in _ocr_cancellation_flags:
            _ocr_cancellation_flags.remove(key)

def find_running_task(user_id, project_id, filename):
    """
    Find a running OCR task MD5 by filename for a specific user and project.
    Used when frontend only has filename but needs to cancel the task.
    """
    with _ocr_status_lock:
        for (uid, pid, md5), status_data in _file_ocr_status.items():
            # Check for match: same user, same project, same filename, and status is running
            if (uid == user_id and 
                pid == project_id and 
                status_data.get('filename') == filename and 
                status_data.get('status') == 'converting'):
                return md5
    return None

def set_file_ocr_status(user_id, project_id, file_md5, filename, status, progress=0, message='', total_pages=0, current_page=0):
    """Set OCR processing status for a file.
    status can be: 'converting', 'completed', 'error'
    """
    with _ocr_status_lock:
        key = (user_id, project_id, file_md5)
        _file_ocr_status[key] = {
            'status': status,
            'filename': filename,
            'progress': progress,
            'message': message,
            'total_pages': total_pages,
            'current_page': current_page,
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        #log_with_timestamp(f"📸 OCR status set: {filename} -> {status} ({progress}%)")

def get_file_ocr_status(user_id, project_id, file_md5):
    """Get OCR status for a specific file.
    Returns None if no OCR is in progress.
    """
    with _ocr_status_lock:
        return _file_ocr_status.get((user_id, project_id, file_md5))

def get_project_ocr_status(user_id, project_id):
    """Get all OCR statuses for files in a project.
    Returns {file_md5: status_dict}
    """
    with _ocr_status_lock:
        result = {}
        for (uid, pid, md5), status in _file_ocr_status.items():
            if uid == user_id and pid == project_id:
                result[md5] = status
        return result

def clear_file_ocr_status(user_id, project_id, file_md5):
    """Clear OCR status for a file (called when OCR completes or fails).
    """
    with _ocr_status_lock:
        key = (user_id, project_id, file_md5)
        if key in _file_ocr_status:
            del _file_ocr_status[key]
            # Also clear any pending cancellation flag to keep set clean
            clear_ocr_cancellation(user_id, project_id, file_md5)
            log_with_timestamp(f"🗑️ OCR status cleared for file {file_md5}")

# ==================== Project Status ====================
# Note: Project status management has been removed as it was only used for contract analysis.
# Cost-ai functionality does not require project status tracking.
