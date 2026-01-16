import re
import json
import ast

# ==================== JSON Helper Functions ====================

def fix_malformed_json_quotes(json_str: str) -> str:
    """Fix unescaped quotes in JSON strings using regex."""
    def escape_quotes_in_value(match):
        key = match.group(1)
        value_with_quotes = match.group(2)
        inner_value = value_with_quotes[1:-1]
        escaped_inner_value = inner_value.replace('"', '\\"')
        return f'{key}: "{escaped_inner_value}"'
    pattern = re.compile(r'("[^"]+")\s*:\s*(".*?")(?=\s*[,}\]])', re.DOTALL)
    return pattern.sub(escape_quotes_in_value, json_str)

def clean_markdown_json(json_str: str) -> str:
    """Remove markdown code fences and other markdown artifacts from JSON string."""
    cleaned = re.sub(r'```json\s*\n?', '', json_str, flags=re.IGNORECASE)
    cleaned = re.sub(r'\n?```', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'^#{1,6}\s+', '', cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r'\*\*(.*?)\*\*', r'\1', cleaned)
    cleaned = re.sub(r'\*(.*?)\*', r'\1', cleaned)
    return cleaned.strip()

def extract_json_fragments(text: str) -> str:
    """Extract the longest JSON fragment from text and attempt basic fixes."""
    json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
    matches = re.findall(json_pattern, text, re.DOTALL)
    if matches:
        longest_match = max(matches, key=len)
        return fix_common_json_issues(longest_match)
    return text

def fix_escape_chars(text: str) -> str:
    """Repair common escape character issues in a string."""
    text = text.replace('\\\"', '"')
    text = re.sub(r'(?<!\\)\"(?![\s,}])', r'\\"', text)
    text = text.replace('\\n', '\n')
    text = re.sub(r'\\t', '\t', text)
    return text

def intelligent_text_repair(text: str) -> str:
    """Apply heuristic fixes to malformed JSON text."""
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'}\s*{', '},{', text)
    text = re.sub(r']\s*{', '],{', text)
    text = re.sub(r'"\s*:', '":', text)
    text = re.sub(r':\s*"([^\"]*)"', r':"\1"', text)
    return text

def remove_think_tags(text: str) -> str:
    """Strip <think>...</think> tags and other XML‑style tags from AI output."""
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'</?thinking>.*?</thinking>', '', text, flags=re.DOTALL | re.IGNORECASE)
    return re.sub(r'\n\s*\n+', '\n', text).strip()

def fix_common_json_issues(json_str: str) -> str:
    """Add missing braces and clean trailing commas in JSON strings."""
    json_str = json_str.strip()
    if not json_str.startswith('{'):
        json_str = '{' + json_str
    if not json_str.endswith('}'):
        json_str = json_str + '}'
    json_str = re.sub(r',\s*}', '}', json_str)
    json_str = re.sub(r',\s*]', ']', json_str)
    return json_str

def clean_control_chars_in_strings(json_str: str) -> str:
    """
    清理 JSON 字符串值内的控制字符（尤其是换行符）
    AI 有时会在字符串内部插入换行或特殊字符导致解析失败
    """
    #  移除字符串内的换行符（保留在字符串外的结构换行）
    # 匹配引号内的内容，将其中的换行替换为空格
    def replace_newlines_in_string(match):
        content = match.group(1)
        # 将换行、回车、制表符等替换为空格
        cleaned = re.sub(r'[\n\r\t]+', ' ', content)
        # 去除多余空格
        cleaned = re.sub(r' +', ' ', cleaned)
        return f'"{cleaned}"'
    
    # 匹配 "..." 字符串（非贪婪，处理转义引号）
    result = re.sub(r'"((?:[^"\\]|\\.)*)"', replace_newlines_in_string, json_str)
    return result


def extract_json_from_response(result):
    """Extract JSON payload from OpenAI‑style response objects.
    
    增强容错：
    1. 支持 ```json``` 标记的内容
    2. 处理 AI 返回多个 JSON 对象的情况（Extra data 错误）
    3. 多种修复策略
    """
    if 'choices' in result and result['choices']:
        content = result['choices'][0]['message']['content']
        
        # 策略1: 提取 ```json``` 标记的内容
        json_match = re.search(r'```json\s*\n(.*?)\n```', content, re.DOTALL)
        if json_match:
            json_str = json_match.group(1).strip()
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                try:
                    return json.loads(fix_malformed_json_quotes(json_str))
                except:
                    pass
        
        # 策略2: 直接解析整个content
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            error_str = str(e)
            
            #  策略3: 处理 "Extra data" 错误（AI返回多个JSON对象）
            if "Extra data" in error_str:
                # 提取第一个完整的 JSON 对象
                first_json = _extract_first_json_object(content)
                if first_json:
                    try:
                        return json.loads(first_json)
                    except:
                        pass
            
            # 策略4: 修复引号问题后解析
            try:
                return json.loads(fix_malformed_json_quotes(content))
            except json.JSONDecodeError:
                # 策略5: 提取最后一个完整的 JSON 对象（有时AI会先输出解释再输出JSON）
                first_json = _extract_first_json_object(content)
                if first_json:
                    try:
                        return json.loads(first_json)
                    except:
                        try:
                            return json.loads(fix_malformed_json_quotes(first_json))
                        except:
                            pass
                
                raise
    
    raise Exception('No valid JSON found in AI response')


def _extract_first_json_object(text: str) -> str:
    """从文本中提取第一个完整的JSON对象（处理嵌套大括号）
    
    用于处理 AI 返回多个 JSON 对象的情况，例如:
    {"a": 1}{"b": 2}  或  {"a": 1} some text {"b": 2}
    """
    # 找到第一个 {
    start = text.find('{')
    if start == -1:
        return None
    
    # 计数括号来找到匹配的 }
    depth = 0
    in_string = False
    escape = False
    
    for i, char in enumerate(text[start:], start):
        if escape:
            escape = False
            continue
        
        if char == '\\':
            escape = True
            continue
        
        if char == '"' and not escape:
            in_string = not in_string
            continue
        
        if in_string:
            continue
        
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0:
                # 找到了匹配的闭括号
                return text[start:i+1]
    
    # 没找到匹配的闭括号，返回None
    return None
