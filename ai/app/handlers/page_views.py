# //app/routes/view_routes.py
from flask import Blueprint, render_template, session, redirect, url_for
from app.config import Config
from app.data_storage.user_manager import init_user_session
from app.cost_ai import cost_ai_bp

view_bp = Blueprint('view', __name__)

# ============================================================================
# 基础路由
# ============================================================================
@view_bp.route('/')
def index():
    """首页 - 重定向到造价AI"""
    init_user_session()  # 自动创建用户session
    return redirect(url_for('cost_ai.cost_ai_page'))

@view_bp.route('/dashboard')
def dashboard():
    """仪表板页面 - 重定向到造价AI"""
    init_user_session()  # 自动创建用户session
    return redirect(url_for('cost_ai.cost_ai_page'))

@view_bp.route('/avatar')
def avatar_selector():
    """头像选择页面"""
    init_user_session()  # 自动创建用户session
    theme = Config.UI_THEME
    template = 'red-avatar.html' if theme == 'red' else 'avatar_selector.html'
    return render_template(template)
