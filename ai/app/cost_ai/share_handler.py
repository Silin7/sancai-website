# app/cost_ai/share_handler.py
# 对话分享处理器
import os
import json
import uuid
from datetime import datetime
from flask import Blueprint, request, jsonify, render_template, session
from app.config import Config
from .conversation_storage import get_conversation, load_conversations

# 分享数据存储目录
SHARE_DATA_DIR = os.path.join(Config.BASE_DIR, 'data', 'cost_ai_shares')

# 分享蓝图
share_bp = Blueprint('cost_ai_share', __name__)

def ensure_share_dir() -> str:
    """确保分享目录存在"""
    os.makedirs(SHARE_DATA_DIR, exist_ok=True)
    return SHARE_DATA_DIR

def get_share_index_file() -> str:
    """获取分享索引文件路径"""
    return os.path.join(ensure_share_dir(), 'index.json')

def load_share_index() -> dict:
    """加载分享索引"""
    file_path = get_share_index_file()
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_share_index(index: dict):
    """保存分享索引"""
    file_path = get_share_index_file()
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

def get_share_file(share_id: str) -> str:
    """获取分享数据文件路径"""
    return os.path.join(ensure_share_dir(), f'{share_id}.json')

def generate_share_id() -> str:
    """生成8位随机分享ID"""
    return str(uuid.uuid4())[:8]

def find_existing_share(user_id: str, conv_id: str) -> str:
    """查找是否已存在该对话的分享"""
    index = load_share_index()
    for share_id, info in index.items():
        if info.get('user_id') == user_id and info.get('conv_id') == conv_id and not info.get('deleted', False):
            return share_id
    return None

def create_share(user_id: str, conv_id: str) -> dict:
    """
    创建对话分享
    
    Args:
        user_id: 用户ID
        conv_id: 对话ID (可能带或不带conv_前缀)
        
    Returns:
        dict: 包含 share_id 和 share_url 的字典
    """
    # 统一处理ID格式：存储中使用的是不带前缀的ID
    short_id = conv_id[5:] if conv_id.startswith('conv_') else conv_id
    
    # 检查是否已有未删除的分享
    existing_share_id = find_existing_share(user_id, short_id)
    if existing_share_id:
        return {
            'share_id': existing_share_id,
            'share_url': f'/cost-ai/share/{existing_share_id}',
            'is_new': False
        }
    
    # 获取对话信息
    conversations = load_conversations(user_id)
    conv_info = None
    for conv in conversations:
        if conv['id'] == short_id:
            conv_info = conv
            break
    
    if not conv_info:
        return None
    
    # 获取对话内容
    conv_data = get_conversation(user_id, short_id)
    
    # 生成分享ID
    share_id = generate_share_id()
    now = datetime.now()
    
    # 创建分享快照
    share_data = {
        'id': share_id,
        'title': conv_info.get('title', '无标题'),
        'messages': conv_data.get('messages', []),
        'created_at': now.isoformat(),
        'user_id': user_id,
        'conv_id': short_id
    }
    
    # 保存分享数据
    share_file = get_share_file(share_id)
    with open(share_file, 'w', encoding='utf-8') as f:
        json.dump(share_data, f, ensure_ascii=False, indent=2)
    
    # 更新索引
    index = load_share_index()
    index[share_id] = {
        'conv_id': short_id,
        'title': conv_info.get('title', '无标题'),
        'created_at': now.isoformat(),
        'user_id': user_id,
        'deleted': False
    }
    save_share_index(index)
    
    return {
        'share_id': share_id,
        'share_url': f'/cost-ai/share/{share_id}',
        'is_new': True
    }

def get_share(share_id: str) -> dict:
    """
    获取分享数据
    
    Args:
        share_id: 分享ID
        
    Returns:
        dict: 分享数据，如果不存在或已删除则返回None
    """
    # 检查索引中是否存在且未删除
    index = load_share_index()
    if share_id not in index or index[share_id].get('deleted', False):
        return None
    
    # 读取分享数据
    share_file = get_share_file(share_id)
    if os.path.exists(share_file):
        with open(share_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def delete_share(share_id: str) -> bool:
    """
    删除分享（软删除）
    
    Args:
        share_id: 分享ID
        
    Returns:
        bool: 是否删除成功
    """
    index = load_share_index()
    if share_id in index:
        index[share_id]['deleted'] = True
        index[share_id]['deleted_at'] = datetime.now().isoformat()
        save_share_index(index)
        return True
    return False

# ==================== API 路由 ====================

@share_bp.route('/api/cost-ai/share/<conv_id>', methods=['POST'])
def create_share_api(conv_id):
    """创建分享链接API"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': '未登录'}), 401
    
    # create_share函数内部会处理ID格式
    result = create_share(user_id, conv_id)
    if result:
        return jsonify({
            'success': True,
            'share_id': result['share_id'],
            'share_url': result['share_url'],
            'is_new': result['is_new']
        })
    else:
        return jsonify({'success': False, 'error': '对话不存在'}), 404

@share_bp.route('/api/cost-ai/share/<share_id>', methods=['DELETE'])
def delete_share_api(share_id):
    """删除分享链接API"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': '未登录'}), 401
    
    # 验证分享是否属于当前用户
    index = load_share_index()
    if share_id not in index:
        return jsonify({'success': False, 'error': '分享不存在'}), 404
    
    if index[share_id].get('user_id') != user_id:
        return jsonify({'success': False, 'error': '无权限'}), 403
    
    if delete_share(share_id):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': '删除失败'}), 500

@share_bp.route('/cost-ai/share/<share_id>')
def view_share(share_id):
    """查看分享页面（公开访问，无需登录）"""
    share_data = get_share(share_id)
    if not share_data:
        return render_template('error.html', 
                             error_title='分享不存在',
                             error_message='该分享链接已失效或不存在'), 404
    
    return render_template('cost-ai-share.html',
                         share_id=share_id,
                         share_data=share_data)
