# app/cost_ai/stream_ai.py
"""
造价AI流式输出模块

封装SSE流式AI调用逻辑，支持逐token输出，实现类似ChatGPT的打字机效果。
当 COST_AI_STREAM_ENABLED 开关关闭时，自动降级为非流式输出。
"""

import json
import requests
from app.config import Config
from app.utils import log_with_timestamp


def _send_dashscope_stream_request(ai_config, headers, payload):
    """
    发送DashScope流式请求
    
    Args:
        ai_config: AI配置字典
        headers: 请求头
        payload: 请求体
        
    Yields:
        str: 每次返回一个文本chunk
    """
    # 获取候选模型列表
    candidates = [ai_config.get("model", "qwen-plus")]
    model_candidates = ai_config.get('model_candidates', [])
    candidates.extend([m for m in model_candidates if m != candidates[0]])
    
    last_error = None
    
    for model_name in candidates:
        payload["model"] = model_name
        payload["stream"] = True
        
        try:
            log_with_timestamp(f"造价AI流式请求: 使用模型 {model_name}")
            
            response = requests.post(
                f"{ai_config['api_base']}/chat/completions",
                headers=headers,
                json=payload,
                timeout=ai_config.get("timeout", 300),
                stream=True
            )
            
            # 检查响应状态
            if response.status_code in [404, 400, 403]:
                try:
                    # 尝试读取错误信息
                    error_text = response.text
                    if 'exhausted' in error_text or 'not_found' in error_text:
                        last_error = f"模型 {model_name} 不可用"
                        log_with_timestamp(last_error)
                        continue
                except:
                    pass
            
            response.raise_for_status()
            
            # 成功，开始流式读取
            if model_name != candidates[0]:
                log_with_timestamp(f"造价AI: 模型 {model_name} 连接成功")
            
            # 迭代读取SSE数据
            full_content = []
            for line in response.iter_lines():
                if line:
                    line_text = line.decode('utf-8')
                    
                    # SSE格式: data: {...}
                    if line_text.startswith('data: '):
                        data_str = line_text[6:]  # 去掉 "data: " 前缀
                        
                        # 检查是否结束
                        if data_str.strip() == '[DONE]':
                            print("\n" + "-"*50)
                            print("【AI 流式返回结束】")
                            print("".join(full_content))
                            print("-"*50 + "\n")
                            return
                        
                        try:
                            data = json.loads(data_str)
                            # 提取delta内容
                            if 'choices' in data and data['choices']:
                                delta = data['choices'][0].get('delta', {})
                                content = delta.get('content', '')
                                if content:
                                    full_content.append(content)
                                    yield content
                        except json.JSONDecodeError:
                            # 忽略无法解析的行
                            continue
            
            # 成功完成，退出循环
            return
            
        except requests.exceptions.RequestException as e:
            last_error = f"模型 {model_name} 请求失败: {str(e)}"
            log_with_timestamp(last_error)
            continue
        except Exception as e:
            last_error = f"模型 {model_name} 未知错误: {str(e)}"
            log_with_timestamp(last_error)
            continue
    
    # 所有模型都失败
    yield f"[错误] 所有模型尝试失败: {last_error}"


def _send_ollama_stream_request(ai_config, prompt, model, timeout):
    """
    发送Ollama流式请求
    
    Args:
        ai_config: AI配置字典
        prompt: 提示词
        model: 模型名称
        timeout: 超时时间
        
    Yields:
        str: 每次返回一个文本chunk
    """
    try:
        log_with_timestamp(f"造价AI流式请求(Ollama): 使用模型 {model}")
        
        payload = {
            "model": model,
            "prompt": prompt,
            "think": False,
            "stream": True
        }
        
        response = requests.post(
            f"{ai_config['api_base']}/api/generate",
            json=payload,
            timeout=timeout,
            stream=True
        )
        
        response.raise_for_status()
        
        log_with_timestamp(f"造价AI(Ollama): 模型 {model} 连接成功")
        full_content_list = []
        
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode('utf-8'))
                    if 'response' in data:
                        content = data['response']
                        full_content_list.append(content)
                        yield content
                    # 检查是否完成
                    if data.get('done', False):
                        print("\n" + "-"*50)
                        print("【AI 流式返回结束 (Ollama)】")
                        print("".join(full_content_list))
                        print("-"*50 + "\n")
                        return
                except json.JSONDecodeError:
                    continue
                    
    except requests.exceptions.Timeout:
        yield f"[错误] Ollama请求超时 (>{timeout}秒)"
    except requests.exceptions.RequestException as e:
        yield f"[错误] Ollama请求异常: {str(e)}"
    except Exception as e:
        yield f"[错误] Ollama调用失败: {str(e)}"


def stream_ai_response(prompt, model=None, timeout=None):
    """
    流式AI响应生成器
    
    根据配置自动路由到不同的AI提供商，支持流式输出。
    当流式开关关闭时，自动降级为非流式输出（一次性返回完整响应）。
    
    Args:
        prompt (str): 用户提示词
        model (str): 可选，指定模型名称
        timeout (int): 可选，超时时间
        
    Yields:
        str: 每次返回一个文本chunk
    """
    # 获取造价AI专用配置
    ai_config = Config.get_cost_ai_config()
    
    # 检查流式开关
    if not ai_config.get('stream_enabled', False):
        # 开关关闭，使用非流式模式
        # 注意：使用造价AI专用配置（COST_AI_MODEL），而不是通用AI配置
        from app.ai_service import _send_dashscope_request_with_retry
        import requests
        
        current_model = model or ai_config.get("model")
        current_timeout = timeout or ai_config.get("timeout", 300)
        
        if ai_config['provider'] == 'ollama':
            # Ollama非流式调用
            try:
                log_with_timestamp(f"造价AI非流式请求(Ollama): 使用模型 {current_model}")
                payload = {
                    "model": current_model,
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
                    yield result['response']
                else:
                    yield f"[错误] Ollama响应格式异常"
            except Exception as e:
                yield f"[错误] Ollama调用失败: {str(e)}"
        else:
            # DashScope / OpenAI 兼容接口非流式调用
            headers = {
                'Authorization': f'Bearer {ai_config["api_key"]}',
                'Content-Type': 'application/json'
            }
            messages = [{"role": "user", "content": prompt}]
            payload = {
                "model": current_model,
                "messages": messages,
                "temperature": ai_config.get("temperature", 0.1),
                "stream": False
            }
            
            # 使用造价AI的模型候选列表进行自动切换
            # 构建临时配置，确保使用造价AI的model_candidates
            cost_ai_config = {
                **ai_config,
                "model": current_model
            }
            
            log_with_timestamp(f"造价AI非流式请求: 使用模型 {current_model}")
            api_result, error = _send_dashscope_request_with_retry(cost_ai_config, headers, payload)
            
            if error:
                yield f"[错误] {error}"
            elif 'choices' in api_result and api_result['choices']:
                yield api_result['choices'][0]['message']['content']
            else:
                yield f"[错误] API响应格式异常"
        return
    
    # 流式模式
    current_model = model or ai_config.get("model")
    current_timeout = timeout or ai_config.get("timeout", 300)
    
    # 打印发送给AI的完整内容
    print("\n" + "="*50)
    print(f"【AI 流式请求 - {current_model}】")
    #print(f"Prompt:\n{prompt}")
    #print('【用户问题：\n】'+prompt.split('用户问题：')[1])
    #print("="*50 + "\n")

    if ai_config['provider'] == 'ollama':
        # Ollama流式
        for chunk in _send_ollama_stream_request(ai_config, prompt, current_model, current_timeout):
            yield chunk
    else:
        # DashScope / OpenAI 兼容接口流式
        headers = {
            'Authorization': f'Bearer {ai_config["api_key"]}',
            'Content-Type': 'application/json'
        }
        
        messages = [{"role": "user", "content": prompt}]
        
        payload = {
            "model": current_model,
            "messages": messages,
            "temperature": ai_config.get("temperature", 0.1),
            "stream": True
        }
        
        # DeepSeek 特有参数
        if ai_config['provider'] == 'deepseek':
            payload["think"] = False
        
        for chunk in _send_dashscope_stream_request(ai_config, headers, payload):
            yield chunk


def get_stream_enabled():
    """
    获取流式输出开关状态
    
    Returns:
        bool: True表示启用流式输出，False表示禁用
    """
    return Config.COST_AI_STREAM_ENABLED
