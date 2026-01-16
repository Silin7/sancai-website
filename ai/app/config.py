# //app/config.py
import os

# 路径配置：获取项目根目录
APP_DIR = os.path.abspath(os.path.dirname(__file__))  # app/ 目录
BASE_DIR = os.path.dirname(APP_DIR)  # 项目根目录（app/ 的上一级）

class Config:
    """应用配置类"""
    # 基础路径配置
    BASE_DIR = BASE_DIR  # 项目根目录
    APP_DIR = APP_DIR    # app 目录
    
    # 密钥配置
    SECRET_KEY = 'a_super_secret_key_for_user_sessions'

    # ==================== 用户管理 ====================
    # Note: 登录功能已移除，系统自动为每个访问者创建用户session
    # 用户ID通过UUID自动生成，无需登录即可使用

    # 路径配置（文件夹位于项目根目录）
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    USER_PROJECTS_FOLDER = os.path.join(BASE_DIR, 'user_projects')

    # 文件配置
    ALLOWED_EXTENSIONS = {'docx', 'pdf', 'doc'}

    # 元数据文件路径
    FILE_MD5_MAPPING = os.path.join(UPLOAD_FOLDER, 'file_md5_mapping.json')
    USERS_MAPPING = os.path.join(USER_PROJECTS_FOLDER, 'users.json')

    # UI主题配置：'red' 或 'default'
    UI_THEME = 'red'
    #UI_THEME = 'default'

    # ==================== AI配置统一管理 ====================
    # AI服务提供商配置---------------------------------------------------------------------------------------------------------------
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'dashscope')  # deepseek, ollama, openai等
    
    # DeepSeek API配置
    DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', 'sk-56ca0d30d5a44e9f9489287099f99c21')
    DEEPSEEK_API_BASE = os.environ.get('DEEPSEEK_API_BASE', 'https://api.deepseek.com')
    
    # OpenAI API配置
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    OPENAI_API_BASE = os.environ.get('OPENAI_API_BASE', 'https://api.openai.com/v1')

    # DASHSCOPE API配置
    DASHSCOPE_API_KEY = os.environ.get('DASHSCOPE_API_KEY', 'sk-b89ac417f67341189eb8ad58654a6522')
    DASHSCOPE_API_BASE = os.environ.get('DASHSCOPE_API_BASE', 'https://dashscope.aliyuncs.com/compatible-mode/v1')
    DASHSCOPE_MODEL = os.environ.get('DASHSCOPE_MODEL', "qwen-plus-0806") 
    
    # DashScope 自动切换的模型候选列表 (当首选模型报错时尝试)
    DASHSCOPE_MODEL_CANDIDATES = [
        "qwen-plus-0919","qwen-plus-1125","qwen-plus-1127","qwen-plus-1220","qwen-plus-2025-01-25",  "qwen-max-2025-01-25","qwen-max","qwen3-max", "qwen-max-latest", "qwen3-max-2025-09-23",  "qwen-plus","qwen-plus-latest"
    ] 
    
    # Ollama配置
    OLLAMA_API_BASE = os.environ.get('OLLAMA_API_BASE', 'http://59.110.18.172:11434')
    OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL', 'deepseek-r1:70b')
    OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL', 'gpt-oss:20b')
    #OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL', 'qwen3:30b')
    OLLAMA_TIMEOUT = int(os.environ.get('OLLAMA_TIMEOUT', '150'))  #超时设置，单位秒
    

    # ==================== OCR配置统一管理 ====================
    # OCR服务提供商配置----------------------------------------------------------------------------------------------------------------
    OCR_PROVIDER = os.environ.get('OCR_PROVIDER', 'dashscope')  # dashscope, deepseek_ollama等
    #OCR_PROVIDER = os.environ.get('OCR_PROVIDER', 'deepseek_ollama')  # dashscope, deepseek_ollama等

    # DeepSeek OCR (Ollama) 配置
    DEEPSEEK_OCR_API_BASE = os.environ.get('DEEPSEEK_OCR_API_BASE', 'http://59.110.18.172:11434')
    #DEEPSEEK_OCR_API_BASE = os.environ.get('DEEPSEEK_OCR_API_BASE', 'http://121.41.34.210:11434')
    DEEPSEEK_OCR_MODEL = os.environ.get('DEEPSEEK_OCR_MODEL', 'deepseek-ocr:latest')
    DEEPSEEK_OCR_TIMEOUT = int(os.environ.get('DEEPSEEK_OCR_TIMEOUT', '150'))

    # ==================== OCR配置（阿里云DashScope） ====================
    # 阿里云DashScope API配置
    DASHSCOPE_API_KEY = os.environ.get('DASHSCOPE_API_KEY', 'sk-b89ac417f67341189eb8ad58654a6522')
    DASHSCOPE_API_BASE = os.environ.get('DASHSCOPE_API_BASE', 'https://dashscope.aliyuncs.com/compatible-mode/v1')
    
    # OCR模型与Chat模型分离
    DASHSCOPE_OCR_MODEL = os.environ.get('DASHSCOPE_OCR_MODEL', 'qwen3-vl-plus')  # 视觉语言模型  qwen-vl-plus qwen3-vl-flash qwen-vl-max qwen-vl-plus 对于如高精度的物体识别与定位（包括 3D 定位）、 Agent 工具调用、文档和网页解析、复杂题目解答、长视频理解等任务，首选 Qwen3-VL，系列内模型对比如下：qwen3-vl-plus：性能最强的模型。qwen3-vl-flash：速度更快，成本更低，是兼顾性能与成本的高性价比选择，适用于对响应速度敏感的场景。对于简单的图像描述、短视频摘要提取等通用任务，可选 Qwen2.5-VL，系列内模型对比如下：qwen-vl-max：Qwen2.5-VL 系列中效果最佳的模型。qwen-vl-plus：速度更快，在效果与成本之间实现良好平衡  https://help.aliyun.com/zh/model-studio/vision?spm=a2c4g.11186623.0.0.6a781edbifetL9#872a5e70bbsu7
    DASHSCOPE_OCR_MODEL = os.environ.get('DASHSCOPE_OCR_MODEL', 'qwen3-vl-flash')  # 视觉语言模型
    DASHSCOPE_OCR_MODEL = os.environ.get('DASHSCOPE_OCR_MODEL', 'qwen-vl-plus') 
    DASHSCOPE_OCR_MODEL = os.environ.get('DASHSCOPE_OCR_MODEL', 'qwen-vl-ocr-latest')  # OCR模型qwen-vl-ocr-2025-04-13
    DASHSCOPE_OCR_MODEL = os.environ.get('DASHSCOPE_OCR_MODEL', "qwen-vl-ocr-2025-04-13")

    # DashScope 自动切换的模型候选列表 (当首选模型报错时尝试)
    DASHSCOPE_OCR_MODEL_CANDIDATES = [
        "qwen-vl-max-2025-04-08","qwen-vl-ocr-2025-08-28","qwen-vl-ocr-2025-11-20","qwen-vl-ocr","qwen-vl-max-2025-04-02","qwen3-vl-plus-2025-12-19","qwen3-vl-plus","qwen-vl-max-2025-08-13","qwen-vl-max"
    ] 


    # 中标通知书 (award) 和 投标文件 (bid) 专用的 OCR 模型
    DASHSCOPE_OCR_MODEL_AWARD_BID = os.environ.get('DASHSCOPE_OCR_MODEL_AWARD_BID', 'qwen-vl-ocr-2025-11-20') # 默认使用更强的模型处理复杂文档
    DASHSCOPE_TIMEOUT = int(os.environ.get('DASHSCOPE_TIMEOUT', '150'))  # OCR超时设置，单位秒
    
    # OCR结果缓存配置
    OCR_CACHE_DIR = os.path.join(UPLOAD_FOLDER, 'ocr_cache')  # OCR结果缓存目录
    OCR_IMAGE_DIR = os.path.join(UPLOAD_FOLDER, 'ocr_images')  # OCR处理图片目录
    OCR_CACHE_FILE = os.path.join(UPLOAD_FOLDER, 'ocr_cache_mapping.json')  # OCR结果映射文件
    
    
    # 通用AI配置
    AI_DEFAULT_MODEL = os.environ.get('AI_DEFAULT_MODEL', 'deepseek-chat')
    AI_TEMPERATURE = float(os.environ.get('AI_TEMPERATURE', '0.1'))
    AI_TIMEOUT = int(os.environ.get('AI_TIMEOUT', '600'))
    
    # ==================== 造价AI数据库配置 ====================
    COST_DB_HOST = os.environ.get('COST_DB_HOST', '59.110.18.172')
    COST_DB_PORT = int(os.environ.get('COST_DB_PORT', '5432'))
    COST_DB_USER = os.environ.get('COST_DB_USER', 'postgres')
    COST_DB_PASSWORD = os.environ.get('COST_DB_PASSWORD', 'rTJNJ66jAmJGsCnt')
    COST_DB_NAME = os.environ.get('COST_DB_NAME', 'newmaterial')
    
    # ==================== 造价AI配置 ====================
    # 造价AI SSE流式输出开关 (true/false)
    # 启用后，AI回复将逐字符流式输出，类似ChatGPT效果
    # 关闭时保持现有的一次性输出行为
    COST_AI_STREAM_ENABLED = os.environ.get('COST_AI_STREAM_ENABLED', 'true').lower() == 'true'
    
    # 造价AI专用模型配置（可选，None表示使用通用AI配置）
    #COST_AI_PROVIDER = os.environ.get('COST_AI_PROVIDER', AI_PROVIDER) # 默认跟随全局AI_PROVIDER
    #COST_AI_MODEL = os.environ.get('COST_AI_MODEL', "qvq-plus-2025-05-15")

    # 造价AI模型候选列表（当首选模型失败时尝试）
    COST_AI_MODEL_DASHSCOPE_CANDIDATES = [
        "qvq-plus-latest", "qvq-max-2025-05-15",  "qvq-max-2025-03-25", "qvq-max-latest", "qwen-plus-0919", "qwen-plus-1125", "qwen-plus-1127", "qwen-plus-1220", "qwen-plus", "qwen-max"
    ]
    
    # 造价AI配置为ollama
    COST_AI_PROVIDER = os.environ.get('COST_AI_PROVIDER', 'ollama')
    COST_AI_MODEL = os.environ.get('COST_AI_MODEL', "qwen3:32b")
   
    
    
    @classmethod
    def get_cost_ai_config(cls):
        """获取造价AI专用配置"""
        provider = cls.COST_AI_PROVIDER
        
        # 基础配置
        config = {
            'stream_enabled': cls.COST_AI_STREAM_ENABLED,
            'model_candidates': cls.COST_AI_MODEL_DASHSCOPE_CANDIDATES,
            'model': cls.COST_AI_MODEL # 优先使用造价专用模型
        }

        if provider == 'ollama':
             config.update({
                'provider': 'ollama',
                'api_base': cls.OLLAMA_API_BASE,
                'timeout': cls.OLLAMA_TIMEOUT,
                'model': cls.COST_AI_MODEL or cls.OLLAMA_MODEL # 如果没配专用模型，作为fallback可以使用通用ollama模型
            })
        elif provider == 'dashscope':
             config.update({
                'provider': 'dashscope',
                'api_key': cls.DASHSCOPE_API_KEY,
                'api_base': cls.DASHSCOPE_API_BASE,
                'timeout': cls.DASHSCOPE_TIMEOUT,
                'model': cls.COST_AI_MODEL or cls.DASHSCOPE_MODEL
            })
        elif provider == 'deepseek':
             config.update({
                'provider': 'deepseek',
                'api_key': cls.DEEPSEEK_API_KEY,
                'api_base': cls.DEEPSEEK_API_BASE,
                'temperature': cls.AI_TEMPERATURE,
                'timeout': cls.AI_TIMEOUT,
                 'model': cls.COST_AI_MODEL or cls.AI_DEFAULT_MODEL
            })
        elif provider == 'openai':
             config.update({
                'provider': 'openai',
                'api_key': cls.OPENAI_API_KEY,
                'api_base': cls.OPENAI_API_BASE,
                'temperature': cls.AI_TEMPERATURE,
                'timeout': cls.AI_TIMEOUT,
                'model': cls.COST_AI_MODEL or cls.AI_DEFAULT_MODEL
            })
        else:
             # Fallback to global config if provider unknown or same as global (simplified logic)
             # 但为了完全解耦，建议显式处理。这里如果 provider 不在上述列表，可能抛错或者回退。
             # 既然允许 COST_AI_PROVIDER 默认为 AI_PROVIDER，那么应该可以复用 get_ai_config 的逻辑，
             # 但必须覆盖 model 等 cost ai 专有属性。
             base_config = cls.get_ai_config()
             base_config.update(config) # Overwrite with cost ai specifics
             return base_config

        return config
    
    @classmethod
    def get_ai_config(cls):
        """获取当前AI配置"""
        if cls.AI_PROVIDER == 'deepseek':
            return {
                'provider': 'deepseek',
                'api_key': cls.DEEPSEEK_API_KEY,
                'api_base': cls.DEEPSEEK_API_BASE,
                'model': cls.AI_DEFAULT_MODEL,
                'temperature': cls.AI_TEMPERATURE,
                'timeout': cls.AI_TIMEOUT
            }
        elif cls.AI_PROVIDER == 'ollama':
            return {
                'provider': 'ollama',
                'api_base': cls.OLLAMA_API_BASE,
                'model': cls.OLLAMA_MODEL,
                'timeout': cls.OLLAMA_TIMEOUT
            }
        elif cls.AI_PROVIDER == 'openai':
            return {
                'provider': 'openai',
                'api_key': cls.OPENAI_API_KEY,
                'api_base': cls.OPENAI_API_BASE,
                'model': cls.AI_DEFAULT_MODEL,
                'temperature': cls.AI_TEMPERATURE,
                'timeout': cls.AI_TIMEOUT
            }
        elif cls.AI_PROVIDER == 'dashscope':
            return {
                'provider': 'dashscope',
                'api_key': cls.DASHSCOPE_API_KEY,
                'api_base': cls.DASHSCOPE_API_BASE,
                'model': cls.DASHSCOPE_MODEL,
                'timeout': cls.DASHSCOPE_TIMEOUT
            }
        else:
            raise ValueError(f"不支持的AI提供商: {cls.AI_PROVIDER}")
    
    @classmethod
    def get_ocr_config(cls, doc_type=None):
        """
        获取OCR专用配置
        
        Args:
            doc_type: 文档类型 (可选，用于OCR配置)
                      如果是 'award' 或 'bid'，将使用专用模型
        """
        if cls.OCR_PROVIDER == 'dashscope':
            # 根据文档类型选择模型
            model = cls.DASHSCOPE_OCR_MODEL
            if doc_type:
                model = cls.DASHSCOPE_OCR_MODEL_AWARD_BID
                
            return {
                'provider': 'dashscope',
                'api_key': cls.DASHSCOPE_API_KEY,
                'api_base': cls.DASHSCOPE_API_BASE,
                'model': model,
                'timeout': cls.DASHSCOPE_TIMEOUT
            }
        elif cls.OCR_PROVIDER == 'deepseek_ollama':
            return {
                'provider': 'deepseek_ollama',
                'api_base': cls.DEEPSEEK_OCR_API_BASE,
                'model': cls.DEEPSEEK_OCR_MODEL,
                'timeout': cls.DEEPSEEK_OCR_TIMEOUT
            }
        else:
            raise ValueError(f"不支持的OCR提供商: {cls.OCR_PROVIDER}")

    # 本地解析库检测
    try:
        import fitz
        import docx
        import requests
        LOCAL_LIBS_INSTALLED = True
        DOCX_AVAILABLE = True
    except ImportError:
        LOCAL_LIBS_INSTALLED = False
        DOCX_AVAILABLE = False