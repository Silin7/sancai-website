# app/cost_ai/query_generator.py
# AI查询生成器
import json
import re
import requests
from app.config import Config
from app.ai_service import _send_dashscope_request_with_retry
from app.utils import log_with_timestamp
from .cost_ai_prompt import (
    SQL_GENERATION_PROMPT, 
    RESULT_FORMAT_PROMPT,
    INTENT_ANALYSIS_PROMPT,
    MULTI_TABLE_SQL_PROMPT
)

# 表名到名称字段的映射
TABLE_NAME_FIELDS = {
    'materials': 'materialname',
    'equipments': 'equipmentname',
    'itproducts': 'itname',
    'humanresources': 'servicename'
}


def _call_cost_ai(prompt: str, timeout=None) -> tuple:
    """
    造价AI专用的AI调用函数（非流式，用于SQL生成和结果格式化）
    
    使用 Config.get_cost_ai_config() 获取造价AI专用配置。
    注意：SQL生成和非流式格式化需要使用纯文本模型，
    因此会自动跳过 qvq 系列视觉语言模型，选择第一个非qvq模型。
    
    Returns:
        tuple: (response_text, error_message)
    """
    ai_config = Config.get_cost_ai_config()
    current_timeout = timeout or ai_config.get("timeout", 300)
    
    # 对于纯文本任务（SQL生成、结果格式化），需要使用非qvq模型
    # qvq是视觉语言模型，不适合纯文本任务
    original_model = ai_config.get("model", "")
    model_candidates = ai_config.get("model_candidates", [])
    
    # 如果当前模型是qvq系列，找第一个非qvq模型
    if 'qvq' in original_model.lower():
        for candidate in model_candidates:
            if 'qvq' not in candidate.lower():
                ai_config = {**ai_config, "model": candidate}
                log_with_timestamp(f"造价AI: SQL生成跳过qvq模型 {original_model}，使用文本模型 {candidate}")
                break
        # 同时过滤候选列表，只保留非qvq模型
        ai_config["model_candidates"] = [m for m in model_candidates if 'qvq' not in m.lower()]
    
    if ai_config['provider'] == 'ollama':
        # Ollama调用
        try:
            payload = {
                "model": ai_config.get("model"),
                "prompt": prompt,
                "think": False,
                "stream": False
            }
            response = requests.post(
                f"{ai_config['api_base']}/api/generate",
                json=payload,
                timeout=current_timeout
            )
            response.raise_for_status()
            result = response.json()
            if 'response' in result:
                return result['response'], None
            else:
                return None, "Ollama响应格式异常"
        except Exception as e:
            return None, f"Ollama调用失败: {str(e)}"
    else:
        # DashScope / OpenAI 兼容接口
        headers = {
            'Authorization': f'Bearer {ai_config["api_key"]}',
            'Content-Type': 'application/json'
        }
        messages = [{"role": "user", "content": prompt}]
        payload = {
            "model": ai_config.get("model"),
            "messages": messages,
            "temperature": ai_config.get("temperature", 0.1),
            "stream": False
        }
        
        log_with_timestamp(f"造价AI (SQL生成): 使用模型 {ai_config.get('model')}")
        
        # 打印发送给AI的完整内容
        print("\n" + "="*50)
        print(f"【AI 请求 - {ai_config.get('model')}】")
        # print(f"Prompt:\n{prompt}")
        print('【用户问题：】\t'+prompt.split('用户问题：')[1])
        # print("="*50 + "\n")
        
        api_result, error = _send_dashscope_request_with_retry(ai_config, headers, payload)
        
        if error:
            print(f"【AI 错误】: {error}\n")
            return None, error
        elif 'choices' in api_result and api_result['choices']:
            response_text = api_result['choices'][0]['message']['content']
            # 打印AI返回的内容
            print("\n" + "-"*50)
            print("【AI 返回】")
            print(response_text)
            print("-"*50 + "\n")
            return response_text, None
        else:
            return None, "API响应格式异常"


def generate_sql(question: str) -> tuple:
    """
    使用AI将自然语言问题转换为SQL查询
    
    Returns:
        tuple: (sql_info, error) - sql_info包含sql、table、description
    """
    prompt = f"{SQL_GENERATION_PROMPT}\n\n用户问题：{question}"
    
    response_text, error = _call_cost_ai(prompt)
    
    if error:
        return None, f"AI调用失败: {error}"
    
    if not response_text:
        return None, "AI返回空响应"
    
    # 解析JSON响应
    try:
        # 尝试提取JSON
        json_match = re.search(r'\{[^{}]*\}', response_text, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
            return result, None
        else:
            # AI没有返回JSON格式，可能是无法理解问题
            # 将AI的文本回复作为description返回，让前端显示给用户
            return {
                "sql": None,
                "table": None,
                "description": response_text.strip()
            }, None
    except json.JSONDecodeError as e:
        # JSON解析失败，同样将原文作为description返回
        return {
            "sql": None,
            "table": None,
            "description": response_text.strip()
        }, None

def format_response(question: str, results: list) -> str:
    """
    使用AI将查询结果格式化为自然语言回答
    
    Returns:
        str: 格式化后的回答
    """
    if not results:
        results_text = "未找到相关数据"
    else:
        # 简化结果，只保留关键字段
        from decimal import Decimal
        simplified = []
        for r in results[:5]:  # 最多显示5条
            item = {}
            # 定义核心关注的字段
            core_keys = ['materialname', 'equipmentname', 'itname', 'servicename', 
                        'brand', 'specification', 'pretaxprice', 'afertaxprice']
            
            # 1. 尝试提取核心字段
            for key in core_keys:
                if key in r:
                    val = r[key]
                    if val is not None and val != "":
                        item[key] = float(val) if isinstance(val, Decimal) else val
            
            # 2. 如果核心字段太少，尝试带上其他非内部字段
            if len(item) < 2:
                for k, v in r.items():
                    if k not in core_keys and k not in ['id', 'status', 'created_at', 'updated_at', 'deleted_at']:
                        if v is not None and v != "":
                            item[k] = float(v) if isinstance(v, Decimal) else v
            
            if item:
                simplified.append(item)
        results_text = json.dumps(simplified, ensure_ascii=False, indent=2)
    
    prompt = RESULT_FORMAT_PROMPT.format(question=question, results=results_text)
    
    response_text, error = _call_cost_ai(prompt)
    
    if error:
        # 如果AI调用失败，返回原始结果
        if not results:
            return "抱歉，未找到相关产品信息。"
        return f"找到以下产品信息：\n{results_text}"
    
    return response_text


def analyze_intent(question: str) -> tuple:
    """
    分析用户问题的意图，判断需要查询哪些表
    
    Returns:
        tuple: (intent_info, error) - intent_info包含tables和reason
    """
    prompt = INTENT_ANALYSIS_PROMPT.format(question=question)
    
    response_text, error = _call_cost_ai(prompt)
    
    if error:
        return None, f"意图分析失败: {error}"
    
    if not response_text:
        return None, "AI返回空响应"
    
    # 解析JSON响应
    try:
        json_match = re.search(r'\{[^{}]*\}', response_text, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
            tables = result.get('tables', [])
            reason = result.get('reason', '')
            
            # 验证表名是否合法
            valid_tables = [t for t in tables if t in TABLE_NAME_FIELDS]
            
            return {
                'tables': valid_tables,
                'reason': reason,
                'is_multi_table': len(valid_tables) > 1
            }, None
        else:
            return {'tables': [], 'reason': '无法解析意图', 'is_multi_table': False}, None
    except json.JSONDecodeError:
        return {'tables': [], 'reason': '解析失败', 'is_multi_table': False}, None


def generate_sql_for_table(question: str, table_name: str) -> tuple:
    """
    为指定的表生成SQL查询
    
    Returns:
        tuple: (sql, error)
    """
    if table_name not in TABLE_NAME_FIELDS:
        return None, f"无效的表名: {table_name}"
    
    name_field = TABLE_NAME_FIELDS[table_name]
    prompt = MULTI_TABLE_SQL_PROMPT.format(
        table_name=table_name,
        name_field=name_field,
        question=question
    )
    
    response_text, error = _call_cost_ai(prompt)
    
    if error:
        return None, f"SQL生成失败: {error}"
    
    if not response_text:
        return None, "AI返回空响应"
    
    # 提取SQL语句（去除markdown代码块标记）
    sql = response_text.strip()
    sql = re.sub(r'^```\w*\n?', '', sql)
    sql = re.sub(r'\n?```$', '', sql)
    sql = sql.strip()
    
    # 基本验证
    if not sql.upper().startswith('SELECT'):
        return None, "生成的不是有效的SELECT语句"
    
    return sql, None

