# //app/contracts_handler/ai_service.py
# AI服务模块 - 统一管理所有AI调用相关功能
import re
import json
import ast
import requests
import time
from .config import Config
from app.utils import log_with_timestamp
from app import json_helpers
# Re-export JSON helper functions for backward compatibility
fix_malformed_json_quotes = json_helpers.fix_malformed_json_quotes
clean_markdown_json = json_helpers.clean_markdown_json
extract_json_fragments = json_helpers.extract_json_fragments
fix_escape_chars = json_helpers.fix_escape_chars
intelligent_text_repair = json_helpers.intelligent_text_repair
remove_think_tags = json_helpers.remove_think_tags
fix_common_json_issues = json_helpers.fix_common_json_issues
extract_json_from_response = json_helpers.extract_json_from_response
clean_control_chars_in_strings = json_helpers.clean_control_chars_in_strings  #  新增：清理字符串内控制字符
import datetime



def _send_dashscope_request_with_retry(ai_config, headers, payload):
    """
    通用 DashScope 请求发送函数，包含自动模型切换逻辑
    Returns:
        tuple: (response_json, error_message)
    """
    # 获取候选模型列表：首选模型 + 备选列表
    # 优先使用传入配置中的model_candidates（如造价AI专用候选列表）
    # 如果没有，则回退使用Config.DASHSCOPE_MODEL_CANDIDATES
    candidates = [ai_config["model"]]
    model_candidates = ai_config.get('model_candidates', [])
    if not model_candidates and hasattr(Config, 'DASHSCOPE_MODEL_CANDIDATES'):
        model_candidates = Config.DASHSCOPE_MODEL_CANDIDATES
    # 过滤掉已经存在的，避免重复尝试
    candidates.extend([m for m in model_candidates if m != ai_config["model"]])
    
    last_error = None
    
    for model_name in candidates:
        payload["model"] = model_name
        try:
            print( f"DashScope: 开始使用模型 {model_name} 进行请求..." )
            if model_name != ai_config["model"]:
                log_with_timestamp(f"DashScope: 尝试切换模型至 {model_name}...")
                
            response = requests.post(f"{ai_config['api_base']}/chat/completions", headers=headers, json=payload, timeout=ai_config["timeout"])
            
            # 检查是否因为模型不存在而失败 (404 或 400 invalid_request_error)
            if response.status_code in [404, 400, 403]:
                try:
                    err_json = response.json()
                    if 'error' in err_json:
                        err_code = err_json['error'].get('code', '')
                        err_msg = err_json['error'].get('message', '')
                        # 如果是模型不存在或不可用，继续下一个
                        if 'The free tier of the model has been exhausted' in err_msg:
                            last_error = f"模型 {model_name}配额不足"
                            log_with_timestamp(last_error)
                            continue
                        if 'model_not_found' in err_code or 'does not exist' in err_msg or 'access' in err_msg:
                            last_error = f"模型 {model_name}不可用: {err_msg}"
                            log_with_timestamp(last_error)
                            continue
                        
                except:
                    pass
            
            response.raise_for_status()
            
            # 如果成功使用备选模型，记录日志
            if model_name != ai_config["model"]:
                log_with_timestamp(f"DashScope: 模型 {model_name} 调用成功，后续将优先使用。")
                Config.DASHSCOPE_MODEL = model_name
                
            return response.json(), None
            
        except requests.exceptions.RequestException as e:
            last_error = f"{ai_config['provider']} ({model_name}) 请求失败: {str(e)}"
            # 如果是特定状态码，可能还是模型问题
            if hasattr(e, 'response') and e.response is not None:
                if e.response.status_code in [404, 400]:
                        log_with_timestamp(f"模型 {model_name} 返回错误状态码 {e.response.status_code}, 尝试下一个...")
                        continue
            
            # 其他错误也继续尝试
            continue
            
        except Exception as e:
                return None, f"未知错误: {str(e)}"
    
    return None, f"DashScope 所有模型尝试失败: {last_error}"


def call_ai_for_part(content, prompt):
    """调用AI进行部分内容分析，返回JSON结果"""
    ai_config = Config.get_ai_config()
    
    
    # 统一处理 OpenAI 兼容的 API (DeepSeek, DashScope, OpenAI)
    if ai_config['provider'] in ['deepseek', 'openai', 'dashscope']:
        headers = {'Authorization': f'Bearer {ai_config["api_key"]}', 'Content-Type': 'application/json'}
        messages = [{"role": "system", "content": prompt}, {"role": "user", "content": f" {content}"}]
        
        # 构建通用 payload
        payload = {
            "model": ai_config["model"], 
            "messages": messages, 
            "temperature": ai_config.get("temperature", 0.7), 
            "stream": False
        }
        
        # DeepSeek 特有参数
        if ai_config['provider'] == 'deepseek':
            payload["think"] = False
            
        # DashScope 自动模型切换逻辑
        if ai_config['provider'] == 'dashscope':
            api_result, error = _send_dashscope_request_with_retry(ai_config, headers, payload)
            if error:
                return None, error
            return extract_json_from_response(api_result), None

        else:
            # DeepSeek, OpenAI 的逻辑 (不带自动切换)
            try:
                response = requests.post(f"{ai_config['api_base']}/chat/completions", headers=headers, json=payload, timeout=ai_config["timeout"])
                response.raise_for_status()
                return extract_json_from_response(response.json()), None
            except Exception as e:
                return None, f"{ai_config['provider']} 请求失败: {str(e)}"
            
    elif ai_config['provider'] == 'ollama':
        # 对于Ollama，需要特殊处理，因为API格式不同
        full_prompt = f"{prompt}\n\n内容：\n{content}"
        response_text, error = call_ollama_ai(full_prompt)
        
        if error:
            return None, error
            
        # 尝试解析返回的文本为JSON字典
        try:
            # 方法1: 提取 ```json ... ``` 标记的内容
            json_match = re.search(r'```json\s*\n(.*?)\n```', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(1).strip()
                result_dict = json.loads(json_str)
                return result_dict, None
            
            # 方法2: 提取 ``` 标记的JSON（不指定语言）
            json_match = re.search(r'```\s*\n(.*?)\n```', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(1).strip()
                result_dict = json.loads(json_str)
                return result_dict, None
            
            # 方法3: 先尝试直接解析JSON
            result_dict = json.loads(response_text)
            return result_dict, None
        except json.JSONDecodeError as e:
            # 增强的JSON解析失败处理
            log_with_timestamp(f"Ollama返回格式异常: {str(e)}")
            
            # 尝试多种修复策略
            repair_strategies = [
                ("清理控制字符", clean_control_chars_in_strings),  #  最常见：AI在字符串内插入换行
                ("移除think标签", remove_think_tags),
                ("修复引号问题", fix_malformed_json_quotes),
                ("清理markdown标记", clean_markdown_json),
                ("提取JSON片段", extract_json_fragments),
                ("修复转义字符", fix_escape_chars),
                ("智能文本修复", intelligent_text_repair)
            ]
            
            for strategy_name, repair_function in repair_strategies:
                try:
                    repaired_text = repair_function(response_text)
                    result_dict = json.loads(repaired_text)
                    log_with_timestamp(f"使用'{strategy_name}'策略修复成功")
                    return result_dict, None
                except Exception as repair_error:
                    log_with_timestamp(f"'{strategy_name}'策略失败: {repair_error}")
                    continue
            
            # 如果所有修复策略都失败，抛出异常
            log_with_timestamp(f"所有修复策略都失败，原始响应: {response_text}")
            return None, f"JSON解析失败: {str(e)}"
    else:
        return None, f"不支持的AI提供商: {ai_config['provider']}"


def call_ai_for_comprehensive_analysis(part1_result, part3_result, prompt):
    """调用AI进行综合分析，基于两个部分的结果"""
    ai_config = Config.get_ai_config()
    
    
    # 统一处理 OpenAI 兼容的 API (DeepSeek, DashScope, OpenAI)
    if ai_config['provider'] in ['deepseek', 'openai', 'dashscope']:
        headers = {'Authorization': f'Bearer {ai_config["api_key"]}', 'Content-Type': 'application/json'}
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"**基础信息数据：**\n{json.dumps(part1_result, ensure_ascii=False, indent=2)}"},
            {"role": "user", "content": f"**条款信息数据：**\n{json.dumps(part3_result, ensure_ascii=False, indent=2)}"},
            {"role": "user", "content": "请基于上述基础信息和条款信息，按照系统提示中的要求进行综合分析并输出JSON结果。"}
        ]

        payload = {
            "model": ai_config["model"], 
            "messages": messages, 
            "temperature": ai_config.get("temperature", 0.7), 
            "stream": False
        }
        
        if ai_config['provider'] == 'dashscope':
            api_result, error = _send_dashscope_request_with_retry(ai_config, headers, payload)
            if error:
                return None, error
            return extract_json_from_response(api_result), None
        else:
            try:
                response = requests.post(f"{ai_config['api_base']}/chat/completions", headers=headers, json=payload, timeout=ai_config["timeout"])
                response.raise_for_status()
                return extract_json_from_response(response.json()), None
            except Exception as e:
                return None, f"{ai_config['provider']} 请求失败: {str(e)}"
            
    elif ai_config['provider'] == 'ollama':
        # 对于Ollama，构建完整提示
        full_prompt = f"""{prompt}

**基础信息数据：**
{json.dumps(part1_result, ensure_ascii=False, indent=2)}

**条款信息数据：**  
{json.dumps(part3_result, ensure_ascii=False, indent=2)}

请基于上述基础信息和条款信息，按照系统提示中的要求进行综合分析并输出JSON结果。"""
        
        response_text, error = call_ollama_ai(full_prompt)
        
        if error:
            return None, error
            
        # 尝试解析返回的文本为JSON字典
        try:
            # 方法1: 提取 ```json ... ``` 标记的内容
            json_match = re.search(r'```json\s*\n(.*?)\n```', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(1).strip()
                result_dict = json.loads(json_str)
                return result_dict, None
            
            # 方法2: 提取 ``` 标记的JSON（不指定语言）
            json_match = re.search(r'```\s*\n(.*?)\n```', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(1).strip()
                result_dict = json.loads(json_str)
                return result_dict, None
            
            # 方法3: 先尝试直接解析JSON
            result_dict = json.loads(response_text)
            return result_dict, None
        except json.JSONDecodeError as e:
            # 增强的JSON解析失败处理
            log_with_timestamp(f"Ollama综合分析返回格式异常: {str(e)}")
            
            # 尝试多种修复策略
            repair_strategies = [
                ("清理控制字符", clean_control_chars_in_strings),  #  最常见：AI在字符串内插入换行
                ("移除think标签", remove_think_tags),
                ("修复引号问题", fix_malformed_json_quotes),
                ("清理markdown标记", clean_markdown_json),
                ("提取JSON片段", extract_json_fragments),
                ("修复转义字符", fix_escape_chars),
                ("智能文本修复", intelligent_text_repair)
            ]
            
            for strategy_name, repair_function in repair_strategies:
                try:
                    repaired_text = repair_function(response_text)
                    result_dict = json.loads(repaired_text)
                    log_with_timestamp(f"使用'{strategy_name}'策略修复成功")
                    return result_dict, None
                except Exception as repair_error:
                    log_with_timestamp(f"'{strategy_name}'策略失败: {repair_error}")
                    continue
            
            # 如果所有修复策略都失败，抛出异常
            log_with_timestamp(f"所有修复策略都失败，原始响应: {response_text[:200]}...")
            return None, f"JSON解析失败: {str(e)}"
    else:
        return None, f"不支持的AI提供商: {ai_config['provider']}"


def call_ai_with_content(content, prompt, model="deepseek-chat", temperature=0.7):
    """
    通用AI调用函数，用于处理任意文本内容和提示词。
    支持不同的模型和温度参数。
    """
    ai_config = Config.get_ai_config()
    headers = {'Authorization': f'Bearer {ai_config["api_key"]}', 'Content-Type': 'application/json'}

    final_prompt = f"{prompt}\n\n请基于以下内容进行分析：\n\n---\n{content}\n---"

    messages = [
        {"role": "system", "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"},
        {"role": "user", "content": final_prompt}
    ]

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "stream": False
    }

    try:
        log_with_timestamp(f"正在调用AI进行分析 (模型: {model}, 温度: {temperature})...")
        response = requests.post(f"{ai_config['api_base']}/chat/completions", headers=headers, json=payload, timeout=180)
        response.raise_for_status()
        result = response.json()
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        else:
            return f"AI响应格式错误: {result}"
    except requests.exceptions.RequestException as e:
        return f"AI分析请求失败: {e}"


def call_ollama_ai(prompt, model=None, timeout=None):
    """
    智能AI调用函数（原名call_ollama_ai，现已升级支持多模型）
    保持函数签名不变，但会根据config.py配置自动路由：
    - 如果配置为ollama：调用本地Ollama
    - 如果配置为dashscope/deepseek等：调用云端API
    
    Args:
        prompt (str): 分析提示词
        model (str): 模型名称，如果为None则使用config中的配置
        timeout (int): 超时时间，如果为None则使用config中的配置
        
    Returns:
        tuple: (response_text, error_message)
    """
    ai_config = Config.get_ai_config()
    
    # 策略路由：如果配置的不是Ollama，自动走通用云端接口
    if ai_config['provider'] != 'ollama':
        try:
            # 复用通用接口的逻辑，但不返回JSON，只返回文本
            #log_with_timestamp(f"call_ollama_ai: 检测到非Ollama配置({ai_config['provider']})，自动切换路由...")
            
            headers = {'Authorization': f'Bearer {ai_config["api_key"]}', 'Content-Type': 'application/json'}
            messages = [{"role": "user", "content": prompt}]
            
            # 优先使用传入的model，否则使用config中的model
            current_model = model or ai_config["model"]
            current_timeout = timeout or ai_config["timeout"]
            
            payload = {
                "model": current_model, 
                "messages": messages, 
                "temperature": ai_config.get("temperature", 0.1), # 保持较低温度以通过测试
                "stream": False
            }
            
            # DeepSeek 特有参数
            if ai_config['provider'] == 'deepseek':
                payload["think"] = False
                
            # DashScope 自动模型切换逻辑
            if ai_config['provider'] == 'dashscope':
                api_result, error = _send_dashscope_request_with_retry(ai_config, headers, payload)
                if error:
                    return None, error
                
                # 提取文本内容
                if 'choices' in api_result and api_result['choices']:
                    return api_result['choices'][0]['message']['content'], None
                else:
                    return None, f"DashScope响应格式异常: {api_result}"
                    
            else:
                # 其他通用OpenAI兼容接口
                response = requests.post(
                    f"{ai_config['api_base']}/chat/completions", 
                    headers=headers, 
                    json=payload, 
                    timeout=current_timeout
                )
                response.raise_for_status()
                result = response.json()
                
                if 'choices' in result and result['choices']:
                    return result['choices'][0]['message']['content'], None
                else:
                    return None, f"API响应格式异常: {result}"
                    
        except Exception as e:
            return None, f"智能路由调用失败: {str(e)}"

    # ==================== 原有的Ollama逻辑 ====================
    # 如果指定了model和timeout参数，使用传入的值；否则使用config中的值
    model = model or ai_config.get('model', 'deepseek-r1:70b')
    timeout = timeout or ai_config.get('timeout', 300)
    
    try:
        #log_with_timestamp(f"正在调用Ollama AI进行分析 (模型: {model})...")
        log_with_timestamp(f"正在调用AI(Ollama)进行分析 ...")
        payload = {
            "model": model,
            "prompt": prompt,
            "think": False,
            "stream": False
        }
        
        start_time = time.time()
        response = requests.post(
            f"{ai_config['api_base']}/api/generate",
            json=payload,
            timeout=timeout
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'response' in result:
                elapsed_time = time.time() - start_time
                log_with_timestamp(f"Ollama AI分析完成，耗时: {elapsed_time:.2f}秒")
                return result['response'], None
            else:
                error_msg = f"Ollama响应格式异常: {result}"
                log_with_timestamp(error_msg)
                return None, error_msg
        else:
            error_msg = f"Ollama请求失败: HTTP {response.status_code}"
            log_with_timestamp(error_msg)
            return None, error_msg
            
    except requests.exceptions.Timeout:
        error_msg = f"Ollama请求超时 (>{timeout}秒)"
        log_with_timestamp(error_msg)
        return None, error_msg
    except requests.exceptions.RequestException as e:
        error_msg = f"Ollama请求异常: {str(e)}"
        log_with_timestamp(error_msg)
        return None, error_msg
    except Exception as e:
        error_msg = f"Ollama调用未知错误: {str(e)}"
        log_with_timestamp(error_msg)
        return None, error_msg


def analyze_document_content(content, filename=""):  #开始时上传文档的分析类型和位置是否正确
    """
    分析文档内容，判断文件类型
    
    Args:
        content (str): 文档内容文本
        filename (str): 文件名，用于辅助判断
        
    Returns:
        dict: 分析结果，包含文件类型、置信度、理由等
    """
    try:
        # 截取前500个字符进行分析
        analysis_content = content[:500] if content else ""
        
        if not analysis_content.strip():
            return {
                'file_type': 'unknown',
                'confidence': 0.0,
                'reason': '文档内容为空或无法解析',
                'method': 'content_analysis'
            }
        
        # 构建分析提示词
        prompt = f"""你是一个专业的文档类型识别专家。请分析以下文档内容的前500个字符，判断它属于以下哪种类型：

1. contract (合同) - 包含合同条款、甲方乙方、合同金额、合同期限等
2. tender (招标文件) - 包含招标公告、技术规格、商务条款、评标标准等  
3. bid (投标文件) - 包含投标报价、技术方案、商务方案、投标函等
4. award (中标通知书) - 包含中标结果、中标金额、中标公告等
5. unknown (无法确定) - 无法明确判断的类型

文件名参考: {filename}

请严格按照以下JSON格式返回结果，不要包含任何其他文字：
{{
    "file_type": "具体的类型名称",
    "confidence": 0.95,
    "reason": "判断理由的详细说明",
    "key_indicators": ["关键词1", "关键词2", "关键词3"],
    "method": "ai_content_analysis"
}}

文档内容预览：
{analysis_content}"""

        # 根据配置调用不同的AI提供商
        ai_config = Config.get_ai_config()
        
        if ai_config['provider'] == 'ollama':
            # 只有明确配置为Ollama时才使用Ollama
            response_text, error = call_ollama_ai(prompt)
        else:
            # 其他情况（DashScope, DeepSeek, OpenAI）使用通用接口
            try:
                # 复用 call_ai_with_content 的逻辑
                headers = {'Authorization': f'Bearer {ai_config["api_key"]}', 'Content-Type': 'application/json'}
                messages = [
                    {"role": "system", "content": "你是一个专业的文档类型识别专家。"},
                    {"role": "user", "content": prompt}
                ]
                
                payload = {
                    "model": ai_config["model"],
                    "messages": messages,
                    "temperature": 0.1, # 使用低温度以获得确定性结果
                    "stream": False
                }
                
                log_with_timestamp(f"文档类型分析 (Provider: {ai_config['provider']})...")
                
                if ai_config['provider'] == 'dashscope':
                     api_result, error = _send_dashscope_request_with_retry(ai_config, headers, payload)
                else:
                    response = requests.post(f"{ai_config['api_base']}/chat/completions", headers=headers, json=payload, timeout=30)
                    response.raise_for_status()
                    api_result = response.json()
                    error = None

                if not error:
                    if 'choices' in api_result and len(api_result['choices']) > 0:
                        response_text = api_result['choices'][0]['message']['content']
                    else:
                        response_text = None
                        error = f"API响应格式错误: {api_result}"
                else:
                    response_text = None
            except Exception as e:
                response_text = None
                error = f"API请求失败: {str(e)}"
        
        if error:
            log_with_timestamp(f"AI分析失败: {error}")
            return {
                'file_type': 'unknown',
                'confidence': 0.0,
                'reason': f'AI分析失败: {error}',
                'method': 'ai_content_analysis'
            }
        
        # 解析AI返回的JSON结果
        try:
            # 尝试多种JSON解析策略
            result = None
            parse_error = None
            
            # 策略1: 尝试直接解析JSON
            try:
                result = json.loads(response_text)
                log_with_timestamp("策略1成功: 直接JSON解析")
            except json.JSONDecodeError as e1:
                parse_error = e1
                log_with_timestamp(f"策略1失败: 直接JSON解析失败: {e1}")
                
                # 策略2: 清理markdown标记后解析
                try:
                    cleaned_text = clean_markdown_json(response_text)
                    result = json.loads(cleaned_text)
                    log_with_timestamp("策略2成功: 清理markdown标记后解析")
                except json.JSONDecodeError as e2:
                    parse_error = e2
                    log_with_timestamp(f"策略2失败: 清理markdown标记失败: {e2}")
                    
                    # 策略3: 提取```json```标记内容后解析
                    try:
                        json_match = re.search(r'```json\s*\n(.*?)\n```', response_text, re.DOTALL)
                        if json_match:
                            json_str = json_match.group(1).strip()
                            result = json.loads(json_str)
                            log_with_timestamp("策略3成功: 提取json标记内容解析")
                        else:
                            raise json.JSONDecodeError("未找到json标记", "", 0)
                    except json.JSONDecodeError as e3:
                        parse_error = e3
                        log_with_timestamp(f"策略3失败: 提取json标记失败: {e3}")
                        
                        # 策略4: 修复常见JSON问题后解析
                        try:
                            fixed_text = fix_malformed_json_quotes(response_text)
                            result = json.loads(fixed_text)
                            log_with_timestamp("策略4成功: 修复JSON格式后解析")
                        except json.JSONDecodeError as e4:
                            parse_error = e4
                            log_with_timestamp(f"策略4失败: 修复JSON格式失败: {e4}")
                            
                            # 策略5: 提取{...}片段后解析
                            try:
                                start_idx = response_text.find('{')
                                end_idx = response_text.rfind('}')
                                if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                                    json_str = response_text[start_idx:end_idx + 1]
                                    result = json.loads(json_str)
                                    log_with_timestamp("策略5成功: 提取JSON片段解析")
                                else:
                                    raise json.JSONDecodeError("未找到JSON片段", "", 0)
                            except json.JSONDecodeError as e5:
                                parse_error = e5
                                log_with_timestamp(f"策略5失败: 提取JSON片段失败: {e5}")
            
            # 如果解析成功，验证和返回结果
            if result is not None:
                if 'file_type' in result:
                    # 确保file_type是有效值
                    valid_types = ['contract', 'tender', 'bid', 'award', 'unknown']
                    if result['file_type'] not in valid_types:
                        result['file_type'] = 'unknown'
                    
                    # 确保confidence是有效值
                    if 'confidence' not in result or not isinstance(result['confidence'], (int, float)):
                        result['confidence'] = 0.5
                    
                    result['method'] = 'ai_content_analysis'
                    log_with_timestamp(f"AI分析成功: {result['file_type']} (置信度: {result['confidence']})")
                    return result
                else:
                    raise ValueError("AI响应中缺少file_type字段")
            else:
                # 所有JSON解析策略都失败，才进入fallback
                log_with_timestamp(f"所有JSON解析策略都失败，错误: {parse_error}")
                log_with_timestamp(f"AI原始响应长度: {len(response_text)} 字符")
                log_with_timestamp(f"AI原始响应前200字符: {response_text[:200]}")
                
                # 尝试从文本中提取文件类型（只作为最后的fallback）
                response_lower = response_text.lower()
                if any(keyword in response_lower for keyword in ['合同', 'contract']):
                    file_type = 'contract'
                elif any(keyword in response_lower for keyword in ['招标', 'tender']):
                    file_type = 'tender'
                elif any(keyword in response_lower for keyword in ['投标', 'bid']):
                    file_type = 'bid'
                elif any(keyword in response_lower for keyword in ['中标', 'award']):
                    file_type = 'award'
                else:
                    file_type = 'unknown'
                
                return {
                    'file_type': file_type,
                    'confidence': 0.3,
                    'reason': f'JSON解析失败，通过关键词匹配推断: {response_text[:100]}',
                    'key_indicators': [],
                    'method': 'ai_content_analysis_fallback'
                }
                
        except Exception as e:
            log_with_timestamp(f"AI响应处理异常: {e}")
            log_with_timestamp(f"AI原始响应: {response_text}")
            
            # 异常情况下的fallback
            return {
                'file_type': 'unknown',
                'confidence': 0.0,
                'reason': f'AI响应处理异常: {str(e)}',
                'key_indicators': [],
                'method': 'ai_content_analysis_error'
            }
            
    except Exception as e:
        error_msg = f"文档内容分析异常: {str(e)}"
        log_with_timestamp(error_msg)
        return {
            'file_type': 'unknown',
            'confidence': 0.0,
            'reason': error_msg,
            'method': 'ai_content_analysis'
        }


def extract_document_preview(file_path, max_chars=500, project_id=None, file_md5=None):
    """
    提取文档内容预览（前N个字符）
    
    注意：DOC转换和图片PDF OCR转换已在上传阶段（process_single_file）完成，
    此函数只负责提取已转换文件的内容。
    
    Args:
        file_path (str): 文件路径（应该已经是转换后的DOCX或文字型PDF）
        max_chars (int): 最大字符数，默认500
        project_id (str): 项目ID（保留参数，向后兼容）
        file_md5 (str): 文件MD5（保留参数，向后兼容）
        
    Returns:
        str: 文档内容预览
    """
    try:
        import os
        file_ext = os.path.splitext(file_path)[1].lower()
        original_filename = os.path.basename(file_path)
        
        # DOC文件应该已在上传阶段转换，如果仍然收到DOC，记录警告
        if file_ext == '.doc':
            log_with_timestamp(f"⚠️ 警告: 收到未转换的DOC文件，应在上传阶段完成转换: {original_filename}")
            # 尝试直接解析（可能会失败）
        
        # 对于PDF，检查是否是图片PDF
        if file_ext == '.pdf':
            try:
                import fitz
                doc = fitz.open(file_path)
                content = "".join([page.get_text() for page in doc])
                doc.close()
                
                if content.strip():
                    # 文字型PDF，直接返回内容
                    return content[:max_chars]
                else:
                    # 图片PDF应该已在上传阶段转换，如果仍然无法提取文字，记录警告
                    log_with_timestamp(f"⚠️ 警告: 图片PDF未经OCR转换，应在上传阶段完成转换: {original_filename}")
                    return ""
                    
            except Exception as pdf_error:
                log_with_timestamp(f"PDF处理失败 {file_path}: {pdf_error}")
                return ""
        
        # 常规文件处理（DOCX等）
        from app.pipeline.preprocess.file_parser import parse_file_locally
        content = parse_file_locally(file_path, enable_ocr=False)  # 不再启用OCR，因为已在上传阶段处理
        
        if content and content.strip():
            return content[:max_chars]
        else:
            return ""
            
    except Exception as e:
        log_with_timestamp(f"提取文档预览失败 {file_path}: {e}")
        return ""

def call_dashscope_ocr_direct(image_path):
    """
    直接调用DashScope OCR API
    
    Args:
        image_path: 图像文件路径
        
    Returns:
        dict: OCR结果
    """
    try:
        config = Config.get_ocr_config()
        
        if not config['api_key']:
            raise Exception("DashScope API Key未配置")
        
        # 导入OCR处理器
        from app.pipeline.preprocess.pdf_ocr_processor import PDFOCRProcessor
        processor = PDFOCRProcessor()
        
        # 编码图像
        image_data = processor.encode_image_to_base64(image_path)
        
        # 构建请求
        headers = {
            'Authorization': f"Bearer {config['api_key']}",
            'Content-Type': 'application/json'
        }
        
        payload = {
            "model": config['model'],
            "input": {
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image_data
                                }
                            },
                            {
                                "type": "text",
                                "text": "请识别并提取图像中的所有文字内容，保持原有格式和结构，直接输出文字内容。"
                            }
                        ]
                    }
                ]
            },
            "parameters": {
                "result_format": "message"
            }
        }
        
        # 发送请求
        import requests
        url = f"{config['api_base']}/chat/completions"
        response = requests.post(
            url, 
            headers=headers, 
            json=payload, 
            timeout=config['timeout']
        )
        response.raise_for_status()
        
        result = response.json()
        
        # 解析结果
        if 'choices' in result and len(result['choices']) > 0:
            content = result['choices'][0]['message']['content']
            ocr_text = content.strip()
            
            return {
                'success': True,
                'text': ocr_text,
                'image_path': image_path,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'api_usage': result.get('usage', {})
            }
        else:
            raise Exception(f"API返回格式异常: {result}")
            
    except Exception as e:
        log_with_timestamp(f"DashScope OCR直接调用失败 {image_path}: {e}")
        return {
            'success': False,
            'error': str(e),
            'image_path': image_path,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


def test_ollama_connection():
    """
    测试Ollama连接是否正常
    
    Returns:
        dict: 测试结果
    """
    try:
        log_with_timestamp("正在测试Ollama连接...")
        
        # 简单的测试提示
        test_prompt = "你好，请简单回复'连接成功'"
        
        response_text, error = call_ollama_ai(test_prompt)
        
        if error:
            return {
                'status': 'failed',
                'error': error,
                'message': 'Ollama连接失败'
            }
        else:
            log_with_timestamp(f"Ollama连接测试成功，响应: {response_text[:50]}")
            return {
                'status': 'success',
                'response': response_text,
                'message': 'Ollama连接正常'
            }
            
    except Exception as e:
        error_msg = f"Ollama连接测试异常: {str(e)}"
        log_with_timestamp(error_msg)
        return {
            'status': 'error',
            'error': error_msg,
            'message': 'Ollama连接测试异常'
        }