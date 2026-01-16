# app/utils.py
# 工具函数合并模块 - 整合日志和SSE管理功能
"""
统一工具模块，包含：
- 日志功能 (原 core_tools/logger.py)
- SSE事件管理 (原 core_tools/sse_manager.py)
"""

import json
import queue
from datetime import datetime

# ============ 日志功能 ============

def log_with_timestamp(message):
    """打印带时间戳的日志"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

# ============ SSE管理功能 ============

# 用户事件队列字典
user_event_queues = {}

def get_or_create_queue(user_id):
    """获取或创建用户的事件队列"""
    if user_id not in user_event_queues:
        user_event_queues[user_id] = queue.Queue()
        log_with_timestamp(f"为用户 {user_id} 创建了新的SSE事件队列。")
    return user_event_queues[user_id]

def push_sse_event(user_id, event_type, data):
    """向指定用户的队列推送一个标准格式的SSE事件。"""
    # 自动创建队列（如果不存在）
    get_or_create_queue(user_id)
    
    if user_id in user_event_queues:
        event_data = {'type': event_type, 'data': data}
        event_str = f"data: {json.dumps(event_data, ensure_ascii=False)}\n\n"
        user_event_queues[user_id].put(event_str)
        log_with_timestamp(f"✅ SSE事件已推送给用户 {user_id}: 类型={event_type}, 数据={str(data)}")
    else:
        log_with_timestamp(f"❌ 错误: 用户 {user_id} 的事件队列不存在，无法推送SSE事件。")

def create_event_stream(user_id):
    """为指定用户创建事件流生成器"""
    if user_id not in user_event_queues:
        user_event_queues[user_id] = queue.Queue()
        log_with_timestamp(f"为用户 {user_id} 创建了新的SSE事件队列。")
    else:
        log_with_timestamp(f"用户 {user_id} 已存在SSE事件队列，复用现有队列。")

    def event_stream():
        try:
            while True:
                try:
                    # 从特定于用户的队列中获取事件
                    yield user_event_queues[user_id].get(timeout=10)
                except queue.Empty:
                    yield "data: {\"type\": \"heartbeat\"}\n\n"
        except GeneratorExit:
            log_with_timestamp(f"用户 {user_id} 的SSE连接已关闭，但将保留其事件队列以供后台线程使用。")

    return event_stream()
