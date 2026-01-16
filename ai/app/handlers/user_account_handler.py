from flask import Blueprint, jsonify, request, session
import os
import threading
import time
from app.ai_service import test_ollama_connection, analyze_document_content
from app.pipeline.preprocess.file_parser import parse_file_locally
from app.data_storage.file_metadata import get_file_by_md5
from app.utils import log_with_timestamp
from app.data_storage.user_manager import init_user_session, ensure_user_has_avatar, get_all_preset_avatars

# Create main blueprint
api_bp = Blueprint('api', __name__)

# 用户信息端点
@api_bp.route('/user/info', methods=['GET'])
def get_user_info():
    """获取当前用户信息"""
    try:
        init_user_session()
        user_id = session.get('user_id')

        if not user_id:
            return jsonify({
                'success': False,
                'error': '用户未初始化'
            }), 401

        # 使用头像管理器确保用户有持久化头像
        avatar, avatar_type = ensure_user_has_avatar(user_id)

        # 更新session中的头像信息
        session['avatar'] = avatar
        session['avatar_type'] = avatar_type

        return jsonify({
            'success': True,
            'user_id': user_id,
            'avatar': avatar,
            'avatar_type': avatar_type,
            'username': f'用户{user_id[:8]}'
        })
    except Exception as e:
        log_with_timestamp(f"获取用户信息异常: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# 头像相关接口
@api_bp.route('/user/avatars', methods=['GET'])
def get_preset_avatars():
    """获取所有预设头像"""
    try:
        avatars = get_all_preset_avatars()
        return jsonify({
            'success': True,
            'avatars': avatars
        })
    except Exception as e:
        log_with_timestamp(f"获取预设头像异常: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/user/avatar', methods=['POST'])
def set_user_avatar():
    """设置用户头像"""
    try:
        init_user_session()
        user_id = session.get('user_id')

        if not user_id:
            return jsonify({
                'success': False,
                'error': '用户未初始化'
            }), 401

        data = request.get_json()
        if not data or 'avatar' not in data:
            return jsonify({
                'success': False,
                'error': '缺少头像参数'
            }), 400

        new_avatar = data['avatar']
        avatar_type = data.get('type', 'preset')

        # 验证头像是否为预设头像之一
        all_avatars = get_all_preset_avatars()
        if new_avatar not in all_avatars['emoji'] and new_avatar not in all_avatars['svg']:
            return jsonify({
                'success': False,
                'error': '无效的头像'
            }), 400

        # 保存新头像
        from app.data_storage.user_manager import save_user_avatar
        if save_user_avatar(user_id, new_avatar, avatar_type):
            session['avatar'] = new_avatar
            session['avatar_type'] = avatar_type

            return jsonify({
                'success': True,
                'message': '头像更新成功',
                'avatar': new_avatar,
                'avatar_type': avatar_type
            })
        else:
            return jsonify({
                'success': False,
                'error': '保存头像失败'
            }), 500

    except Exception as e:
        log_with_timestamp(f"设置用户头像异常: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# Register sub-blueprints
# Note: Contract-related blueprints have been removed, only cost-ai functionality remains

# AI测试端点
@api_bp.route('/test-ai', methods=['GET'])
def test_ai_connection():
    """测试AI服务连接"""
    try:
        result = test_ollama_connection()
        return jsonify(result)
    except Exception as e:
        log_with_timestamp(f"AI连接测试异常: {e}")
        return jsonify({
            'status': 'error',
            'error': str(e),
            'message': 'AI连接测试失败'
        }), 500

@api_bp.route('/analyze-file', methods=['POST'])
def analyze_file_content():
    """分析上传的文件内容"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': '未找到文件'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': '文件名不能为空'}), 400

        # 保存临时文件
        import tempfile
        import os

        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, file.filename)
        file.save(temp_path)

        try:
            # 解析文件内容
            content = parse_file_locally(temp_path)

            if not content:
                return jsonify({
                    'error': '文件内容无法解析',
                    'file_type': 'unknown'
                }), 400

            # 提取前500字符进行分析
            preview_content = content[:500]

            # 使用AI分析
            ai_result = analyze_document_content(content, file.filename)

            return jsonify({
                'success': True,
                'filename': file.filename,
                'content_length': len(content),
                'preview_length': len(preview_content),
                'ai_analysis': ai_result,
                'preview_content': preview_content
            })

        finally:
            # 清理临时文件
            if os.path.exists(temp_path):
                os.remove(temp_path)

    except Exception as e:
        log_with_timestamp(f"文件分析异常: {e}")
        return jsonify({
            'error': f'文件分析失败: {str(e)}',
            'file_type': 'unknown'
        }), 500

# 🆕 文件预览URL缓存 - 后端内存缓存机制
_preview_url_cache = {}
_preview_url_cache_lock = threading.Lock()
_preview_cache_timeout = 30 * 60  # 30分钟缓存超时
_preview_cache_max_size = 1000    # 最大缓存条目数

def _get_preview_cache_key(file_md5, filename):
    """生成预览URL缓存键"""
    return f"{file_md5}_{filename}"

def _get_cached_preview_url(file_md5, filename):
    """从缓存获取预览URL"""
    with _preview_url_cache_lock:
        cache_key = _get_preview_cache_key(file_md5, filename)
        if cache_key in _preview_url_cache:
            cache_entry = _preview_url_cache[cache_key]
            # 检查是否超时
            if time.time() - cache_entry['timestamp'] < _preview_cache_timeout:
                log_with_timestamp(f"✨ 使用缓存的预览URL: {file_md5}")
                return cache_entry
            else:
                # 缓存超时，删除
                del _preview_url_cache[cache_key]
        return None

def _cache_preview_url(file_md5, filename, file_url, file_info):
    """缓存预览URL"""
    with _preview_url_cache_lock:
        cache_key = _get_preview_cache_key(file_md5, filename)

        # 如果缓存已满，删除最旧的条目
        if len(_preview_url_cache) >= _preview_cache_max_size:
            # 删除最旧的条目
            oldest_key = min(_preview_url_cache.keys(),
                           key=lambda k: _preview_url_cache[k]['timestamp'])
            del _preview_url_cache[ oldest_key]
            log_with_timestamp(f"🧹 清理预览URL缓存，删除最旧条目: {oldest_key}")

        # 添加新缓存
        _preview_url_cache[cache_key] = {
            'file_url': file_url,
            'filename': file_info.get('filename', filename),
            'file_size': file_info.get('file_size', 0),
            'timestamp': time.time()
        }

        log_with_timestamp(f"💾 缓存预览URL: {file_md5}")

# 文件预览URL获取端点 - 增强版（支持后端缓存）
@api_bp.route('/preview/file/url', methods=['POST'])
def get_preview_file_url():
    """根据MD5获取文件预览URL（专门用于文件预览功能）"""
    try:
        import time  # 确保time模块已导入

        data = request.get_json()
        if not data:
            log_with_timestamp(f"❌ 文件URL请求失败: 请求数据为空")
            return jsonify({
                'success': False,
                'error': '请求数据为空'
            }), 400

        file_md5 = data.get('file_md5')
        filename = data.get('filename')  # 用于日志

        log_with_timestamp(f"🔍 收到文件预览URL请求: MD5={file_md5}, 文件名={filename}")

        if not file_md5:
            log_with_timestamp(f"❌ 文件预览URL请求失败: 缺少file_md5参数")
            return jsonify({
                'success': False,
                'error': '缺少必要参数：file_md5'
            }), 400

        # 🆕 优先检查后端缓存
        cached_result = _get_cached_preview_url(file_md5, filename)
        if cached_result:
            log_with_timestamp(f"✨ 使用后端缓存的预览URL: {file_md5}")
            return jsonify({
                'success': True,
                'file_url': cached_result['file_url'],
                'filename': cached_result['filename'],
                'file_size': cached_result['file_size'],
                'cached': True
            })

        # 通过MD5查找文件（前端传递的MD5已经是转换后文件的MD5）
        file_path, file_info = get_file_by_md5(file_md5)

        log_with_timestamp(f"🔍 预览文件MD5查找结果: 路径={file_path}, 信息={file_info}")

        if not file_path or not os.path.exists(file_path):
            log_with_timestamp(f"❌ 文件预览URL请求失败: 文件不存在 MD5={file_md5}")
            return jsonify({
                'success': False,
                'error': '文件不存在或已删除',
                'debug_info': {
                    'searched_md5': file_md5,
                    'file_path': file_path,
                    'file_exists': os.path.exists(file_path) if file_path else False
                }
            }), 404

        # 构建文件URL
        from app.config import Config

        # 处理路径（支持子文件夹，如OCR文件夹）
        if Config.UPLOAD_FOLDER in file_path:
            # 文件在uploads目录内，使用相对路径
            relative_path = os.path.relpath(file_path, Config.UPLOAD_FOLDER)
            file_url = f'/uploads/{relative_path.replace(os.sep, "/")}'
        else:
            # 文件在其他位置
            relative_path = os.path.relpath(file_path, Config.BASE_DIR)
            file_url = f'/{relative_path.replace(os.sep, "/")}'

        log_with_timestamp(f"✅ 通过MD5获取文件预览URL成功: MD5={file_md5}, 文件={filename}, 路径={file_path}, URL={file_url}")

        # 🆕 缓存结果到后端内存
        _cache_preview_url(file_md5, filename, file_url, file_info)

        return jsonify({
            'success': True,
            'file_url': file_url,
            'filename': file_info.get('filename', filename),
            'file_size': file_info.get('file_size', 0),
            'cached': False
        })

    except Exception as e:
        log_with_timestamp(f"❌ 获取文件预览URL异常: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'获取文件预览URL失败: {str(e)}'
        }), 500
