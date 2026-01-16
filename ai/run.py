# /run.py
from flask import Flask
import os
from app.config import Config
from app.register_routes import register_routes
from app.utils import log_with_timestamp

# --- 路径配置 ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, 
           template_folder=os.path.join(BASE_DIR, 'app', 'templates'),
           static_folder=os.path.join(BASE_DIR, 'app', 'static'))

# 允许URL尾部斜杠的灵活性
app.url_map.strict_slashes = False

# --- 应用配置 ---
app.config.from_object(Config)

# --- 注册路由 ---
register_routes(app)

# --- 模板上下文处理器：自动注入主题路径 ---
@app.context_processor
def inject_theme():
    """为所有模板注入主题相关变量"""
    if Config.UI_THEME == 'red':
        css_prefix = 'red-'
    else:
        css_prefix = ''
    return {'theme_css_prefix': css_prefix}

# --- 自动创建用户session ---
@app.before_request
def auto_init_session():
    """自动为所有请求创建用户session（如果不存在）"""
    from flask import request, session
    from app.data_storage.user_manager import init_user_session
    
    # 静态文件和分享页面不需要session
    if request.path.startswith('/static') or request.path.startswith('/cost-ai/share'):
        return None
    
    # 自动初始化用户session
    init_user_session()
    return None

# --- 目录初始化 ---
for folder in [app.config['UPLOAD_FOLDER'], Config.USER_PROJECTS_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# --- 启动说明 ---
# 推荐使用 Flask 命令行工具来启动应用，以获得更好的控制和灵活性。
# 在启动前，请根据您的操作系统，在终端中设置环境变量:
#
# Windows (cmd.exe):
# set FLASK_APP=app.py
#
# Windows (PowerShell):
# $env:FLASK_APP = "app.py"
#
# Linux/macOS:
# export FLASK_APP=app.py
#
# ---
#
# 启动命令:
#
# 1. 开发模式 (代码修改后会自动重载):
# flask run --host=0.0.0.0
#
# 2. 稳定分析模式 (禁用自动重载，防止分析任务被中断):
# flask run --host=0.0.0.0 --no-reload
#
if __name__ == '__main__':
    log_with_timestamp("Flask 造价AI助手系统启动")
    app.run(host='0.0.0.0', port=5000, debug=True)  #