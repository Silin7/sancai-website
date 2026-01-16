# //app/routes.py
# 路由注册文件
from flask import send_from_directory, send_file, abort
from .handlers.user_account_handler import api_bp
from .handlers.event_stream_handler import sse_bp
from .handlers.page_views import view_bp
from .cost_ai import cost_ai_bp, share_bp
from .config import Config
from .utils import log_with_timestamp
import os

def register_routes(app):
    """注册所有路由"""
    #  改进的uploads目录静态文件服务（支持OCR子文件夹）
    @app.route('/uploads/<path:filename>')  # 🆕 使用<path:>支持子路径
    def uploaded_file(filename):
        """提供uploads目录及其子目录下的文件访问"""
        try:
            #  构建文件路径
            file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
            
            log_with_timestamp(f"尝试访问文件: {filename}")
            log_with_timestamp(f"完整路径: {file_path}")
            
            # 🆕 检查文件是否存在
            if not os.path.exists(file_path):
                log_with_timestamp(f"文件不存在: {file_path}")
                
                #  尝试在uploads目录及其子目录中搜索
                try:
                    # 递归搜索uploads目录及其子目录
                    for root, dirs, files in os.walk(Config.UPLOAD_FOLDER):
                        for f in files:
                            if filename in f or f == filename:
                                full_path = os.path.join(root, f)
                                log_with_timestamp(f"在子目录中找到匹配文件: {full_path}")
                                return send_file(full_path, as_attachment=False)
                    
                    #  列出uploads目录结构进行调试
                    files = []
                    for root, dirs, dir_files in os.walk(Config.UPLOAD_FOLDER):
                        for f in dir_files:
                            rel_path = os.path.relpath(os.path.join(root, f), Config.UPLOAD_FOLDER)
                            files.append(rel_path)
                    
                    log_with_timestamp(f"uploads目录结构: {files}")
                    
                except Exception as walk_error:
                    log_with_timestamp(f"目录搜索失败: {walk_error}")
                
                abort(404)
            
            log_with_timestamp(f"文件存在，正在发送: {file_path}")
            # 使用send_file支持更好的中文文件名处理
            return send_file(file_path, as_attachment=False)
            
        except Exception as e:
            log_with_timestamp(f"文件服务错误: {e}")
            abort(500)
    
    app.register_blueprint(view_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(sse_bp, url_prefix='/sse')
    app.register_blueprint(cost_ai_bp)  # ✅ 注册造价AI路由
    app.register_blueprint(share_bp)  # ✅ 注册分享路由