# app/data_storage/user_manager.py
"""
用户数据管理模块
整合用户会话、头像、历史记录和文件元数据管理功能

原模块:
- users_manager/user_manager.py
- users_manager/avatar_manager.py
- users_manager/handle_user_history_json.py
"""

import os
import json
import uuid
import random
import threading
from datetime import datetime
from flask import session, url_for
from ..config import Config
from ..utils import log_with_timestamp

# ============ 路径配置 ============
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(BASE_DIR))
USER_DATA_DIR = os.path.join(PROJECT_ROOT, 'user_data')

# ============ 头像配置 ============
USE_EMOJI_AVATARS = True

SVG_AVATARS = [
    # 1. 渐变商务风 - 专业蓝紫渐变
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad1)"/>
        <circle cx="50" cy="35" r="14" fill="#ffffff" opacity="0.9"/>
        <ellipse cx="50" cy="75" rx="24" ry="28" fill="#ffffff" opacity="0.9"/>
    </svg>''',
    
    # 2. 温柔粉色系 - 柔和女性风格
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#fbc2eb;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#a6c1ee;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad2)"/>
        <circle cx="50" cy="38" r="15" fill="#ffffff" opacity="0.85"/>
        <path d="M 30 75 Q 50 85 70 75 L 70 95 L 30 95 Z" fill="#ffffff" opacity="0.85"/>
    </svg>''',
    
    # 3. 活力橙粉 - 年轻阳光
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad3" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#f093fb;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#f5576c;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad3)"/>
        <circle cx="50" cy="38" r="15" fill="#ffffff" opacity="0.9"/>
        <rect x="30" y="58" width="40" height="38" rx="10" fill="#ffffff" opacity="0.9"/>  
    </svg>''',
    
    # 4. 科技蓝绿 - 现代科技感
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad4" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad4)"/>
        <circle cx="50" cy="36" r="15" fill="#ffffff" opacity="0.9"/>
        <path d="M 25 70 L 35 60 L 65 60 L 75 70 L 75 95 L 25 95 Z" fill="#ffffff" opacity="0.9"/>
    </svg>''',
    
    # 5. 优雅紫罗兰 - 高端典雅
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad5" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#a8edea;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#fed6e3;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad5)"/>
        <circle cx="50" cy="37" r="16" fill="#ffffff" opacity="0.85"/>
        <ellipse cx="50" cy="75" rx="26" ry="30" fill="#ffffff" opacity="0.85"/>
    </svg>''',
    
    # 6. 自然绿色 - 清新自然
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad6" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#56ab2f;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#a8e063;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad6)"/>
        <circle cx="50" cy="36" r="14" fill="#ffffff" opacity="0.9"/>
        <path d="M 28 68 Q 50 78 72 68 L 72 95 L 28 95 Z" fill="#ffffff" opacity="0.9"/>
    </svg>''',
    
    # 7. 热情红色 - 活力动感
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad7" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#eb3349;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#f45c43;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad7)"/>
        <circle cx="50" cy="38" r="15" fill="#ffffff" opacity="0.9"/>
        <rect x="30" y="58" width="40" height="38" rx="10" fill="#ffffff" opacity="0.9"/>  
    </svg>''',
    
    # 8. 深邃靛蓝 - 沉稳专业
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad8" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#2c3e50;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#3498db;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad8)"/>
        <circle cx="50" cy="36" r="14" fill="#ffffff" opacity="0.9"/>
        <path d="M 27 70 L 35 60 L 65 60 L 73 70 L 73 95 L 27 95 Z" fill="#ffffff" opacity="0.9"/>
    </svg>''',
    
    # 9. 薄荷青色 - 清爽舒适
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad9" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#43e97b;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#38f9d7;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad9)"/>
        <circle cx="50" cy="35" r="15" fill="#ffffff" opacity="0.9"/>
        <ellipse cx="50" cy="72" rx="25" ry="29" fill="#ffffff" opacity="0.9"/>
    </svg>''',
    
    # 10. 日落暖色 - 温暖友好
    '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad10" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#fa709a;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#fee140;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="50" fill="url(#grad10)"/>
        <circle cx="50" cy="37" r="16" fill="#ffffff" opacity="0.88"/>
        <path d="M 30 73 Q 50 82 70 73 L 70 95 L 30 95 Z" fill="#ffffff" opacity="0.88"/>
    </svg>'''
]



EMOJI_AVATARS = [
    '🐯', '🐘', '🦉', '🐢', '🐳', '🌳', '🌵', '🌸', '🍁', '🍄',
    '👨‍💼', '👩‍💼', '👨‍🔧', '👩‍🔧', '👨‍🍳', '👩‍🍳', '👨‍🎨', '👩‍🎨', '⭐', '🔥'
]

# ============ 元数据文件锁 ============
file_metadata_lock = threading.Lock()

# ============ 用户会话管理 ============

def init_user_session():
    """
    自动初始化用户会话。
    如果session中没有user_id，则自动分配一个UUID作为用户ID。
    同时确保用户有头像。
    
    返回: True 表示会话已初始化
    """
    # 如果session中没有user_id，自动创建一个
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
        user_id = session['user_id']
        log_with_timestamp(f"[Session] 自动创建用户session: {user_id[:8]}")
        
        # 确保用户有头像
        avatar, avatar_type = ensure_user_has_avatar(user_id)
        session['avatar'] = avatar
        session['avatar_type'] = avatar_type
    else:
        # 已有user_id，确保有头像
        user_id = session['user_id']
        if 'avatar' not in session:
            avatar, avatar_type = ensure_user_has_avatar(user_id)
            session['avatar'] = avatar
            session['avatar_type'] = avatar_type
    
    return True


# Note: verify_user and is_authenticated functions have been removed
# as login functionality is no longer required. All users are automatically
# assigned a session via init_user_session().

# ============ 用户历史记录 ============

def get_user_history():
    """获取当前用户的历史记录"""
    if 'user_id' not in session:
        return []
    
    user_id = session['user_id']
    history_file = os.path.join(USER_DATA_DIR, f"{user_id}.json")
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# ============ 头像管理 ============

def get_avatar_file_path(user_id):
    """获取用户头像文件路径"""
    return os.path.join(USER_DATA_DIR, f"{user_id}_avatar.json")

def load_user_avatar(user_id):
    """加载用户头像"""
    avatar_file = get_avatar_file_path(user_id)
    if os.path.exists(avatar_file):
        try:
            with open(avatar_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('avatar'), data.get('type', 'preset')
        except:
            pass
    return None, None

def save_user_avatar(user_id, avatar, avatar_type='preset'):
    """保存用户头像"""
    # 确保user_data目录存在
    os.makedirs(USER_DATA_DIR, exist_ok=True)
    
    avatar_file = get_avatar_file_path(user_id)
    try:
        with open(avatar_file, 'w', encoding='utf-8') as f:
            json.dump({
                'avatar': avatar,
                'type': avatar_type,
                'updated_time': datetime.now().isoformat()
            }, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        log_with_timestamp(f"保存用户头像失败 {user_id}: {e}")
        return False

def get_random_avatar():
    """获取随机头像"""
    if USE_EMOJI_AVATARS:
        return random.choice(EMOJI_AVATARS)
    else:
        return random.choice(SVG_AVATARS)

def ensure_user_has_avatar(user_id):
    """确保用户有头像，如果不存在则分配一个"""
    avatar, avatar_type = load_user_avatar(user_id)
    
    if not avatar:
        avatar = get_random_avatar()
        avatar_type = 'preset'
        save_user_avatar(user_id, avatar, avatar_type)
        log_with_timestamp(f"为新用户 {user_id[:8]} 分配头像: {type(avatar).__name__} (长度: {len(avatar)})")
    
    return avatar, avatar_type

def get_all_preset_avatars():
    """获取所有预设头像"""
    return {
        'emoji': EMOJI_AVATARS,
        'svg': SVG_AVATARS,
        'current_type': 'emoji' if USE_EMOJI_AVATARS else 'svg'
    }

# ============ 文件元数据（原 handle_user_history_json.py）============

def load_metadata():
    """加载文件元数据JSON文件"""
    if not os.path.exists(Config.FILE_METADATA_PATH):
        return {}
    try:
        with open(Config.FILE_METADATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_metadata(data):
    """保存文件元数据到JSON文件"""
    # 确保目录存在
    os.makedirs(os.path.dirname(Config.FILE_METADATA_PATH), exist_ok=True)
    with open(Config.FILE_METADATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
