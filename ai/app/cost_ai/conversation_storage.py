# app/cost_ai/conversation_storage.py
# 对话历史存储服务
import os
import json
import uuid
from datetime import datetime
from app.config import Config

# 存储目录
COST_AI_DATA_DIR = os.path.join(Config.BASE_DIR, 'user_cost_ai')

# 软删除模式开关
SOFT_DELETE_MODE = False

def ensure_user_dir(user_id: str) -> str:
    """确保用户目录存在"""
    user_dir = os.path.join(COST_AI_DATA_DIR, user_id)
    os.makedirs(user_dir, exist_ok=True)
    return user_dir

def get_conversations_file(user_id: str) -> str:
    """获取用户对话列表文件路径"""
    return os.path.join(ensure_user_dir(user_id), 'conversations.json')

def load_conversations(user_id: str) -> list:
    """加载用户所有对话列表"""
    file_path = get_conversations_file(user_id)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            conversations = json.load(f)
            # 过滤掉已删除的对话
            return [c for c in conversations if not c.get('deleted', False)]
    return []

def save_conversations(user_id: str, conversations: list):
    """保存用户对话列表"""
    file_path = get_conversations_file(user_id)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(conversations, f, ensure_ascii=False, indent=2)

def get_conversation_file(user_id: str, conv_id: str) -> str:
    """获取单个对话文件路径"""
    return os.path.join(ensure_user_dir(user_id), f'conv_{conv_id}.json')

def create_conversation(user_id: str, title: str = "新对话") -> dict:
    """创建新对话"""
    conv_id = str(uuid.uuid4())[:8]
    now = datetime.now()
    
    conversation = {
        'id': conv_id,
        'title': title,
        'created_at': now.isoformat(),
        'updated_at': now.isoformat(),
        'message_count': 0,
        'deleted': False
    }
    
    # 更新对话列表
    conversations = load_conversations(user_id)
    conversations.insert(0, conversation)  # 新对话放在最前面
    save_conversations(user_id, conversations)
    
    # 创建对话消息文件
    conv_file = get_conversation_file(user_id, conv_id)
    with open(conv_file, 'w', encoding='utf-8') as f:
        json.dump({'messages': []}, f, ensure_ascii=False)
    
    return conversation

def get_conversation(user_id: str, conv_id: str) -> dict:
    """获取对话详情（包含消息）"""
    conv_file = get_conversation_file(user_id, conv_id)
    if os.path.exists(conv_file):
        with open(conv_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'messages': []}

def add_message(user_id: str, conv_id: str, role: str, content: str, pair_id: int = None) -> dict:
    """添加消息到对话"""
    conv_file = get_conversation_file(user_id, conv_id)
    now = datetime.now()
    
    # 加载并更新对话消息
    conv_data = get_conversation(user_id, conv_id)
    messages = conv_data.get('messages', [])
    
    # 计算 pair_id（如果未手动指定）
    if pair_id is None:
        if role == 'user':
            # 用户消息：找最大的 pair_id 并加 1
            max_pair_id = 0
            for m in messages:
                if 'pair_id' in m:
                    max_pair_id = max(max_pair_id, m['pair_id'])
            pair_id = max_pair_id + 1
        else:
            # AI 消息：找最后一个用户消息的 pair_id
            pair_id = 1
            for m in reversed(messages):
                if m['role'] == 'user' and 'pair_id' in m:
                    pair_id = m['pair_id']
                    break

    message = {
        'role': role,  # 'user' or 'assistant'
        'content': content,
        'pair_id': pair_id,
        'time': now.strftime('%H:%M'),
        'timestamp': now.isoformat()
    }
    
    # 如果是 AI 回答，初始化版本列表
    if role == 'assistant':
        message['versions'] = [content]
        message['active_index'] = 0
    
    messages.append(message)
    conv_data['messages'] = messages
    
    with open(conv_file, 'w', encoding='utf-8') as f:
        json.dump(conv_data, f, ensure_ascii=False, indent=2)
    
    # 更新对话列表中的信息
    conversations = load_conversations(user_id)
    for conv in conversations:
        if conv['id'] == conv_id:
            conv['updated_at'] = now.isoformat()
            conv['message_count'] = len(messages)
            # 用第一条用户消息作为标题
            if conv['title'] == '新对话' and role == 'user':
                conv['title'] = content[:20] + ('...' if len(content) > 20 else '')
            break
    save_conversations(user_id, conversations)
    
    return message

def add_message_version(user_id: str, conv_id: str, pair_id: int, content: str) -> dict:
    """为指定 pair_id 的 AI 消息添加新版本"""
    conv_file = get_conversation_file(user_id, conv_id)
    conv_data = get_conversation(user_id, conv_id)
    messages = conv_data.get('messages', [])
    
    for msg in messages:
        if msg['role'] == 'assistant' and msg.get('pair_id') == pair_id:
            if 'versions' not in msg:
                msg['versions'] = [msg['content']]
            
            msg['versions'].append(content)
            msg['active_index'] = len(msg['versions']) - 1
            msg['content'] = content # 更新当前展示内容
            break
            
    with open(conv_file, 'w', encoding='utf-8') as f:
        json.dump(conv_data, f, ensure_ascii=False, indent=2)
    
    return conv_data

def update_message_time(user_id: str, conv_id: str, pair_id: int) -> bool:
    """更新指定 pair_id 的消息时间（通常用于重试或重新生成时刷新时间戳）"""
    conv_file = get_conversation_file(user_id, conv_id)
    conv_data = get_conversation(user_id, conv_id)
    messages = conv_data.get('messages', [])
    
    updated = False
    now = datetime.now()
    new_time = now.strftime('%H:%M')
    new_timestamp = now.isoformat()
    
    for msg in messages:
        if msg.get('pair_id') == pair_id:
            msg['time'] = new_time
            msg['timestamp'] = new_timestamp
            updated = True
            # 注意：此处不 break，因为可能想同时更新 user 和 assistant 的时间（如果存在）
            
    if updated:
        with open(conv_file, 'w', encoding='utf-8') as f:
            json.dump(conv_data, f, ensure_ascii=False, indent=2)
            
    return updated

def switch_message_version(user_id: str, conv_id: str, pair_id: int, version_index: int) -> bool:
    """切换指定 pair_id 的 AI 消息显示版本"""
    conv_file = get_conversation_file(user_id, conv_id)
    conv_data = get_conversation(user_id, conv_id)
    messages = conv_data.get('messages', [])
    updated = False
    
    for msg in messages:
        if msg['role'] == 'assistant' and msg.get('pair_id') == pair_id:
            if 'versions' in msg and 0 <= version_index < len(msg['versions']):
                msg['active_index'] = version_index
                msg['content'] = msg['versions'][version_index]
                updated = True
                break
                
    if updated:
        with open(conv_file, 'w', encoding='utf-8') as f:
            json.dump(conv_data, f, ensure_ascii=False, indent=2)
            
    return updated

def delete_conversation(user_id: str, conv_id: str) -> bool:
    """删除对话"""
    import logging
    logger = logging.getLogger(__name__)
    
    if SOFT_DELETE_MODE:
        # 软删除：仅标记 deleted=True，不删除文件
        logger.info(f"软删除模式：标记对话 {conv_id} 为已删除")
        
        file_path = get_conversations_file(user_id)
        if not os.path.exists(file_path):
            logger.warning(f"对话列表文件不存在: {file_path}")
            return False
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                all_conversations = json.load(f)
            
            updated = False
            for conv in all_conversations:
                if conv['id'] == conv_id:
                    conv['deleted'] = True
                    conv['deleted_at'] = datetime.now().isoformat()
                    updated = True
                    logger.info(f"标记对话 {conv_id} 为已删除")
                    break
            
            if updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(all_conversations, f, ensure_ascii=False, indent=2)
                logger.info(f"成功保存软删除状态到 {file_path}")
                return True
            else:
                logger.warning(f"未找到对话 {conv_id} 在列表中")
                return False
                
        except Exception as e:
            logger.error(f"软删除对话 {conv_id} 失败: {e}")
            return False

    else:
        # 硬删除：物理删除文件和列表条目
        logger.info(f"硬删除模式：删除对话 {conv_id} 的文件和列表条目")
        
        # 1. 删除对话内容文件 conv_[id].json
        conv_file = get_conversation_file(user_id, conv_id)
        if os.path.exists(conv_file):
            try:
                os.remove(conv_file)
                logger.info(f"成功删除对话文件: {conv_file}")
            except PermissionError as e:
                logger.error(f"文件被锁定，无法删除 {conv_file}: {e}")
                # 继续执行，至少从列表中移除
            except Exception as e:
                logger.error(f"删除对话文件失败 {conv_file}: {e}")
        else:
            logger.warning(f"对话文件不存在，跳过删除: {conv_file}")
        
        # 2. 从 conversations.json 列表中移除条目
        file_path = get_conversations_file(user_id)
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    all_conversations = json.load(f)
                
                original_count = len(all_conversations)
                new_conversations = [c for c in all_conversations if c['id'] != conv_id]
                removed_count = original_count - len(new_conversations)
                
                if removed_count > 0:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(new_conversations, f, ensure_ascii=False, indent=2)
                    logger.info(f"从列表中移除对话 {conv_id}，共移除 {removed_count} 条")
                else:
                    logger.warning(f"未在列表中找到对话 {conv_id}")
                    
            except Exception as e:
                logger.error(f"从列表中移除对话 {conv_id} 失败: {e}")
                return False
        else:
            logger.warning(f"对话列表文件不存在: {file_path}")
        
        return True

def update_conversation_title(user_id: str, conv_id: str, new_title: str) -> bool:
    """更新对话标题"""
    conversations = load_conversations(user_id)
    updated = False
    
    for conv in conversations:
        if conv['id'] == conv_id:
            conv['title'] = new_title
            conv['updated_at'] = datetime.now().isoformat()
            updated = True
            break
            
    if updated:
        save_conversations(user_id, conversations)
        
    return updated
