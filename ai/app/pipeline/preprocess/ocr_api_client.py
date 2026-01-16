# app/pipeline/preprocess/ocr_api_client.py
# 阿里云 DashScope OCR API 调用模块
# 从 pdf_ocr_processor.py 拆分

import os
import base64
import time
import requests
import urllib3
from datetime import datetime
from ...config import Config
from ...utils import log_with_timestamp

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DashScopeOCRClient:
    """阿里云 DashScope OCR API 客户端"""
    
    def __init__(self, config=None, doc_type=None):
        """
        初始化 OCR 客户端
        
        Args:
            config: OCR配置字典，如果不提供则从Config获取
            doc_type: 文档类型 (传给 Config.get_ocr_config)
        """
        self.config = config or Config.get_ocr_config(doc_type=doc_type)
    
    def _extract_page_number(self, image_path):
        """
        安全地从图像路径中提取页码
        
        Args:
            image_path: 图像文件路径
            
        Returns:
            int: 页码，如果无法提取则返回0
        """
        try:
            basename = os.path.splitext(os.path.basename(image_path))[0]
            if '_' in basename:
                last_part = basename.split('_')[-1]
                # 尝试将最后一部分转换为整数
                if last_part.isdigit():
                    return int(last_part)
            return 0
        except Exception:
            return 0

    def encode_image_to_base64(self, image_path):
        """将图像文件编码为base64字符串"""
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                return f"data:image/png;base64,{encoded_string}"
        except Exception as e:
            log_with_timestamp(f"图像编码失败 {image_path}: {e}")
            raise e

    def _send_ocr_request_with_retry(self, headers, payload, is_vl_chat=False):
        """
        发送OCR请求，包含自动模型切换逻辑
        
        Args:
            headers: 请求头
            payload: 请求体
            is_vl_chat: 是否为 VL Chat 模式 (非 OCR 专用模式)
            
        Returns:
            tuple: (response_json, error_message)
        """
        # 获取候选模型列表：首选模型 + 备选列表
        current_model = payload.get("model", self.config["model"])
        candidates = [current_model]
        
        # 获取备选模型列表
        candidate_list = []
        if hasattr(Config, 'DASHSCOPE_OCR_MODEL_CANDIDATES'):
            candidate_list = Config.DASHSCOPE_OCR_MODEL_CANDIDATES
        elif hasattr(Config, 'DASHSCOPE_MODEL_CANDIDATES'):
            # 后备：使用通用的候选列表
            candidate_list = Config.DASHSCOPE_MODEL_CANDIDATES
            
        if candidate_list:
            # 过滤掉已经存在的，避免重复尝试
            candidates.extend([m for m in candidate_list if m != current_model])
        
        last_error = None
        
        for model_name in candidates:
            payload["model"] = model_name
            
            # 如果是 OCR 模式切换模型，需要检查模型是否支持 OCR 参数
            # qwen-vl-ocr 系列支持 ocr_options，其他通用 VL 模型可能不支持或不需要
            # 这里简单处理：如果切换到了非 OCR 专用模型，可能需要移除 ocr_options，但目前假设候选列表都是兼容的
            
            try:
                if model_name != current_model:
                    log_with_timestamp(f"DashScope OCR: 尝试切换模型至 {model_name}...")
                    
                response = requests.post(
                    f"{self.config['api_base']}/chat/completions", 
                    headers=headers, 
                    json=payload, 
                    timeout=self.config["timeout"],
                    verify=False
                )
                
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
                            if 'model_not_found' in err_code or 'does not exist' in err_msg or 'access' in err_msg or 'Forbidden' in err_msg:
                                last_error = f"模型 {model_name}不可用: {err_msg}"
                                log_with_timestamp(last_error)
                                continue
                    except:
                        pass
                
                # 检查特殊错误
                if response.status_code == 400 and "DataInspectionFailed" in response.text:
                   last_error = f"模型 {model_name} 图片审核失败，尝试下一个模型"
                   log_with_timestamp(last_error)
                   continue

                response.raise_for_status()
                
                # 如果成功使用备选模型，记录日志
                if model_name != current_model:
                    log_with_timestamp(f"DashScope OCR: 模型 {model_name} 调用成功。")
                    
                return response.json(), None
                
            except requests.exceptions.RequestException as e:
                last_error = f"请求失败 ({model_name}): {str(e)}"
                # 如果是特定状态码，可能还是模型问题
                if hasattr(e, 'response') and e.response is not None:
                    if e.response.status_code in [403, 404, 400]:
                            log_with_timestamp(f"模型 {model_name} 返回错误状态码 {e.response.status_code}, 尝试下一个...")
                            continue
                
                # 其他错误也继续尝试
                continue
                
            except Exception as e:
                    return None, f"未知错误: {str(e)}"
        
        return None, f"DashScope OCR 所有模型尝试失败: {last_error}"
    
    @staticmethod
    def extract_text_from_ocr_result(ocr_result):
        """
        从 DashScope OCR 高精模式的 ocr_result 中提取纯文字
        
        Args:
            ocr_result: ocr_result 对象，包含 words_info 数组
            
        Returns:
            str: 提取的纯文字，按顺序拼接
        """
        if not ocr_result:
            return ""
        
        words_list = []
        # 兼容两种格式: 
        # 1. 字典格式: {'words_info': [...]}
        # 2. 列表格式: [{}, {}...] (qwen-vl-ocr-latest 可能直接返回列表)
        if isinstance(ocr_result, dict) and 'words_info' in ocr_result:
            words_list = ocr_result['words_info']
        elif isinstance(ocr_result, list):
            words_list = ocr_result
            
        texts = [item.get('text', '') for item in words_list if isinstance(item, dict)]
        return '\n'.join(texts)

    
    def call_ocr(self, image_path, max_retries=10):
        """
        调用阿里云DashScope API进行OCR - 支持重试机制和自动模型切换
        """
        last_error = None
        
        # 预先读取并编码图像
        try:
            with open(image_path, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            return {
                'success': False,
                'error': f"读取图像失败: {str(e)}",
                'image_path': image_path,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'retry_count': 0
            }

        # 初始模型配置
        model_name = self.config.get('model', '')  
        # 记录本次调用的当前模型（可能会在重试中切换，但不影响 self.config）
        current_model_name = model_name
        
        # 判断初始模型是否为 OCR 专用模型
        is_ocr_model = 'ocr' in current_model_name.lower() or 'vl' in current_model_name.lower() 
        
        # rotate_rect 错误计数器，用于决定是否切换模型
        rotate_rect_error_count = 0
        
        # --- 硬编码配置 ---
        # 遇到 rotate_rect 错误时，在当前模型重试的次数。
        # 0 = 不重试，直接切模型
        # 1 = 重试1次，如果还不行，切模型
        ROTATE_RECT_RETRIES_BEFORE_SWITCH = 0
        # ----------------
        
        # 获取候选模型列表
        candidates = [current_model_name]
        candidate_list = []
        if hasattr(Config, 'DASHSCOPE_OCR_MODEL_CANDIDATES'):
            candidate_list = Config.DASHSCOPE_OCR_MODEL_CANDIDATES
        elif hasattr(Config, 'DASHSCOPE_MODEL_CANDIDATES'):
            candidate_list = Config.DASHSCOPE_MODEL_CANDIDATES
            
        if candidate_list:
            candidates.extend([m for m in candidate_list if m != current_model_name])
        
        # 候选模型索引
        candidate_index = 0
        
        # 注意：这里的 max_retries 是针对整个流程的重试（包括文件读取等），
        # 但 _send_ocr_request_with_retry 内部已经有了模型轮询机制。
        # 为了保持兼容性，我们保留外层循环，但主要依赖内部的模型切换。
        
        for attempt in range(max_retries):
            try:
                if not self.config['api_key']:
                    raise Exception("DashScope API Key未配置")
                
                # 构建请求
                headers = {
                    'Authorization': f"Bearer {self.config['api_key']}",
                    'Content-Type': 'application/json'
                }
                
                payload = {
                    "model": current_model_name,
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/png;base64,{image_base64}"
                                    }
                                },
                                {
                                    "type": "text",
                                    "text": "请识别并提取图像中的所有文字内容，保持原有格式和结构，直接输出文字内容，不要额外的解释说明。"
                                }
                            ]
                        }
                    ],
                    "max_tokens": 4096
                }
                
                # 只有当原始配置的模型确实是预期的高精 OCR 模型时，才添加 task 参数
                # 注意：如果切换到了备选模型，可能需要依据备选模型的能力来调整。
                # 但目前假设 CANDIDATES 里的模型都尽量兼容或足够智能。
                # qwen-vl-ocr-* 系列需要 task 参数来开启高精模式
                if 'ocr' in current_model_name.lower():
                    payload['ocr_options'] = {
                        "task": "advanced_recognition"
                    }
                
                mode_desc = "高精OCR" if 'ocr' in current_model_name.lower() else "普通VL"
                log_with_timestamp(f"正在调用DashScope {mode_desc} 【{current_model_name}】 API处理图像: {os.path.basename(image_path)} (尝试 {attempt + 1}/{max_retries})")
                
                # 使用带有模型切换的新发送函数
                # 注意：这里我们已经在外层处理模型切换逻辑，_send_ocr_request_with_retry 
                # 内部其实也有模型切换逻辑，这可能会导致双重切换。
                # 为了精确控制 "rotate_rect 错误切模型"，我们最好直接调用 requests 或者是简化 _send_ocr_request_with_retry
                # 但为了最小化改动，我们继续使用它，但要注意它内部主要处理的是 404/400 等网络/参数级错误。
                # 而 rotate_rect 是业务逻辑级错误 (返回了 200 但内容无法解析)。
                
                # 为了避免混淆，我们可以只使用 _send_ocr_request_with_retry 的基本发送功能，
                # 或者更简单地，由于我们现在要控 current_model_name，
                # 实际上 _send_ocr_request_with_retry 内部的 candidates 逻辑可能会干扰。
                # 但查看源码，它会优先使用 payload['model']。
                
                # 这里为了简单直接，我们直接复用 _send_ocr_request_with_retry，
                # 只要 payload['model'] 是我们想要的 current_model_name 即可。
                # _send_ocr_request_with_retry 会基于 payload['model'] 初始化 candidates，
                # 如果它失败了且不是 rotate_rect 错误，它内部会切模型。
                result, error = self._send_ocr_request_with_retry(headers, payload)
                
                if error:
                    raise Exception(error)
                
                if not result:
                    raise Exception("API返回空结果")

                # 解析结果
                if 'choices' in result and len(result['choices']) > 0:
                    message_content = result['choices'][0]['message']['content']
                    
                    # 重新判断当前实际使用的模型（因为可能发生了切换）
                    used_model = result.get('model', current_model_name)
                    is_ocr_result = 'ocr' in used_model.lower()
                    
                    ocr_result = None
                    
                    # 尝试解析 OCR 结果
                    # 1. 结构化 List
                    if isinstance(message_content, list) and len(message_content) > 0:
                        first = message_content[0]
                        if isinstance(first, dict):
                            ocr_result = first.get('ocr_result')

                    # 2. Markdown JSON / JSON String
                    if not ocr_result and isinstance(message_content, str):
                        import re
                        import json
                        # 尝试提取 markdown json
                        json_pattern = r'```(?:json)?\s*(\[.*?\]|\{.*?\})\s*```'
                        match = re.search(json_pattern, message_content, re.DOTALL)
                        if match:
                            try:
                                json_str = match.group(1)
                                parsed = json.loads(json_str)
                                if isinstance(parsed, dict) and 'words_info' in parsed:
                                     ocr_result = parsed
                                elif isinstance(parsed, list):
                                     ocr_result = parsed
                            except:
                                pass
                        
                        # 尝试直接 JSON
                        if not ocr_result:
                            try:
                                stripped = message_content.strip()
                                if stripped.startswith(('[', '{')):
                                    parsed = json.loads(stripped)
                                    if isinstance(parsed, dict) and 'words_info' in parsed:
                                         ocr_result = parsed
                                    elif isinstance(parsed, list):
                                         ocr_result = parsed
                            except:
                                pass

                    if ocr_result:
                        # 成功解析出 OCR 结果
                        ocr_text = self.extract_text_from_ocr_result(ocr_result)
                        
                        if 'rotate_rect' in ocr_text  or "###" in ocr_text or "**" in ocr_text or "section" in ocr_text:
                             raise Exception(f"OCR结果被识别为原始JSON结构，视为无效结果需重试。")
                             
                        log_with_timestamp(f"DashScope 高精OCR成功 ({used_model}): {os.path.basename(image_path)} - 提取{len(ocr_text)}字符")
                        
                        return {
                            'success': True,
                            'text': ocr_text,
                            'ocr_result': ocr_result,
                            'text_with_bbox': ocr_result,
                            'image_path': image_path,
                            'page_number': self._extract_page_number(image_path),
                            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            'provider': 'dashscope_ocr',
                            'api_usage': result.get('usage', {}),
                            'retry_count': attempt,
                            'model_used': used_model
                        }
                    else:
                        # 普通文本模式
                        if isinstance(message_content, list) and len(message_content) > 0:
                             ocr_text = message_content[0].get('text', '').strip()
                        else:
                             ocr_text = message_content.strip() if isinstance(message_content, str) else str(message_content)
                        
                        if 'rotate_rect' in ocr_text  or "###" in ocr_text or "**" in ocr_text or "section" in ocr_text:
                            raise Exception(f"OCR结果包含原始JSON结构（rotate_rect），验证失败需重试")
                    
                    log_with_timestamp(f"DashScope OCR成功 ({used_model}): {os.path.basename(image_path)} - 提取{len(ocr_text)}字符")
                    
                    return {
                        'success': True,
                        'text': ocr_text,
                        'image_path': image_path,
                        'page_number': self._extract_page_number(image_path),
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'provider': 'dashscope',
                        'api_usage': result.get('usage', {}),
                        'retry_count': attempt,
                        'model_used': used_model
                    }

                else:
                    raise Exception(f"API返回格式异常: {result}")
            
            except Exception as e:
                error_msg = str(e)
                last_error = f"DashScope OCR处理失败: {error_msg}"
                log_with_timestamp(f"{last_error} - 尝试 {attempt + 1}/{max_retries}")
                
                # ---------------------------------------------------------
                # rotate_rect 专用重试与模型切换逻辑
                # ---------------------------------------------------------
                if "rotate_rect" in error_msg:
                    rotate_rect_error_count += 1
                    
                    if rotate_rect_error_count > ROTATE_RECT_RETRIES_BEFORE_SWITCH:
                        # 错误次数超过重试阈值，切换模型
                        log_with_timestamp(f"模型 {current_model_name} 连续 {rotate_rect_error_count} 次出现 rotate_rect 解析错误，准备切换模型...")
                        
                        # 寻找下一个候选模型
                        # 简单地在 candidates 列表中循环
                        candidate_index = (candidate_index + 1) % len(candidates)
                        new_model = candidates[candidate_index]
                        
                        if new_model != current_model_name:
                            log_with_timestamp(f"已从 {current_model_name} 切换至 {new_model}")
                            current_model_name = new_model
                            # 重置计数器，给新模型同样的机会
                            rotate_rect_error_count = 0
                    else:
                        log_with_timestamp(f"模型 {current_model_name} 出现 rotate_rect 解析错误，将在该模型上重试 ({rotate_rect_error_count}/{ROTATE_RECT_RETRIES_BEFORE_SWITCH})...")
                # ---------------------------------------------------------
                
                # 如果不是最后一次尝试，等待一段时间后重试
                if attempt < max_retries - 1:
                    wait_time = 5
                    time.sleep(wait_time)
        
        return {
            'success': False,
            'error': last_error,
            'image_path': image_path,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'retry_count': max_retries
        }


    def call_vl_chat(self, image_path, prompt, max_retries=3):
        """
        调用 VL 模型进行对话 (非 OCR 模式)
        
        Args:
            image_path: 图片路径
            prompt: 提示词
            max_retries: 重试次数
            
        Returns:
            str: 模型回复内容
        """
        last_error = None
        for attempt in range(max_retries):
            try:
                # 编码图像
                with open(image_path, "rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
                
                headers = {
                    'Authorization': f"Bearer {self.config['api_key']}",
                    'Content-Type': 'application/json'
                }
                
                # 选择模型：从候选列表中找不带 ocr 的通用 VL 模型
                model_name = self.config['model']
                if 'ocr' in model_name.lower():
                    # 当前模型是 OCR 专用模型，需要从候选列表找通用 VL 模型
                    candidate_list = []
                    if hasattr(Config, 'DASHSCOPE_OCR_MODEL_CANDIDATES'):
                        candidate_list = Config.DASHSCOPE_OCR_MODEL_CANDIDATES
                    elif hasattr(Config, 'DASHSCOPE_MODEL_CANDIDATES'):
                        candidate_list = Config.DASHSCOPE_MODEL_CANDIDATES
                    
                    # 从候选列表中找不带 ocr 的模型
                    vl_model = None
                    for candidate in candidate_list:
                        vl_model = "qwen3-vl-flash-2025-10-15"
                        break
                        # if candidate.lower() == "qwen-vl-max":
                        #     vl_model = candidate
                        #     break
                        # if 'ocr' not in candidate.lower():
                        #     vl_model = candidate
                        #     break
                    
                    if vl_model:
                        model_name = vl_model
                        log_with_timestamp(f"  [VL Chat] OCR 模型不适用，已从候选列表切换至 {model_name}")
                    else:
                        raise Exception(f"VL Chat 错误：候选模型列表中没有找到不带 OCR 的通用 VL 模型，无法进行方向判断！候选列表: {candidate_list}")
                
                # 使用普通 VL 模式的 payload
                payload = {
                    "model": model_name,
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/png;base64,{image_base64}"
                                    }
                                },
                                {
                                    "type": "text",
                                    "text": prompt
                                }
                            ]
                        }
                    ],
                    "max_tokens": 512
                }
                
                url = f"{self.config['api_base']}/chat/completions"
                
                # 使用带有重试和模型切换的发送函数
                result, error = self._send_ocr_request_with_retry(headers, payload, is_vl_chat=True)
                
                if error:
                    raise Exception(error)
                
                if 'choices' in result and len(result['choices']) > 0:
                    content = result['choices'][0]['message']['content']
                    return content
                else:
                    raise Exception(f"API返回空结果: {result}")
                    
            except Exception as e:
                last_error = str(e)
                log_with_timestamp(f"VL调用失败 (尝试 {attempt+1}): {e}")
                time.sleep(1)
        
        raise Exception(f"VL调用最终失败: {last_error}")


# 便捷函数
def call_dashscope_ocr(image_path, max_retries=10, config=None, doc_type=None):
    """
    便捷函数：调用 DashScope OCR API
    
    Args:
        image_path: 图像文件路径
        max_retries: 最大重试次数
        config: 可选的配置字典
        doc_type: 文档类型
        
    Returns:
        dict: OCR结果
    """
    client = DashScopeOCRClient(config, doc_type=doc_type)
    return client.call_ocr(image_path, max_retries)
