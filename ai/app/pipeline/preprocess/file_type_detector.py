# app/pipeline/preprocess/file_type_detector.py
# 文件类型检测器 - 通过分析文件内容来判断文件类型
import re
import os
from .file_parser import parse_file_locally
from ...utils import log_with_timestamp
from app.ai_service import analyze_document_content, extract_document_preview


def detect_file_type_ai(file_path, filename="", project_id=None, file_md5=None):    #上传时文件校验的主入口
    """
    使用AI检测文件类型（主要方法）
    在此阶段进行DOC和图片PDF的转换
    
    Args:
        file_path: 文件路径
        filename: 文件名（仅用于日志）
        project_id: 项目ID（用于OCR/DOC转换后更新映射）
        file_md5: 文件MD5（用于OCR/DOC转换后更新映射）
    
    Returns:
        str: 文件类型 ('contract', 'tender', 'bid', 'award', 'unknown')
    """
    try:
        log_with_timestamp(f"开始AI检测文件类型: {filename}")
        
        # ✅ 方法1: 优先使用AI分析
        # 提取文档内容前500字符（在此阶段会自动处理DOC和图片PDF转换）
        content_preview = extract_document_preview(
            file_path,
            max_chars=500,
            project_id=project_id,
            file_md5=file_md5
        )
        
        if content_preview:
            # 使用AI分析文档内容
            ai_result = analyze_document_content(content_preview, filename)
            
            if ai_result and ai_result.get('file_type') != 'unknown':
                detected_type = ai_result['file_type']
                confidence = ai_result.get('confidence', 0.0)
                reason = ai_result.get('reason', '')
                
                log_with_timestamp(f"AI分析成功: {filename} -> {detected_type} (置信度: {confidence:.2f})")
                
                # 如果置信度足够高，直接返回AI结果
                if confidence >= 0.7:
                    return detected_type
                else:
                    log_with_timestamp(f"AI置信度较低 ({confidence:.2f})，使用备用方法验证: {filename}")
                    # 置信度不够高，继续使用备用方法
            else:
                log_with_timestamp(f"AI分析未能确定类型或返回unknown，使用备用方法: {filename}")
        else:
            log_with_timestamp(f"无法提取文档内容，使用备用方法: {filename}")
        
        # ✅ 方法2: 如果AI分析失败，使用备用方法验证
        fallback_result = detect_file_type_fallback(file_path, filename)
        
        if fallback_result != 'unknown':
            log_with_timestamp(f"备用方法验证成功: {filename} -> {fallback_result}")
            return fallback_result
        else:
            log_with_timestamp(f"AI和备用方法都无法确定文件类型: {filename}")
            return 'unknown'
        
    except Exception as e:
        log_with_timestamp(f"AI文件类型检测出错 {filename}: {e}")
        # AI失败时回退到备用方法
        try:
            fallback_result = detect_file_type_fallback(file_path, filename)
            log_with_timestamp(f"AI出错后备用方法结果: {filename} -> {fallback_result}")
            return fallback_result
        except Exception as fallback_error:
            log_with_timestamp(f"备用方法也失败 {filename}: {fallback_error}")
            return 'unknown'

def detect_file_type(file_path, filename="", project_id=None, file_md5=None):
    """
    检测文件类型（通过AI，这是主要接口）
    
    Args:
        file_path: 文件路径
        filename: 文件名（仅用于日志）
        project_id: 项目ID（用于转换后更新映射）
        file_md5: 文件MD5（用于转换后更新映射）
    
    Returns:
        str: 文件类型 ('contract', 'tender', 'bid', 'award', 'unknown')
    """
    return detect_file_type_ai(file_path, filename, project_id, file_md5)

def detect_file_type_fallback(file_path, filename=""):
    """
    文件类型检测备用方法（仅在AI不可用时使用）
    
    Args:
        file_path: 文件路径
        filename: 文件名（用于辅助判断）
    
    Returns:
        str: 文件类型 ('contract', 'tender', 'bid', 'award', 'unknown')
    """
    try:
        # 解析文件内容
        content = parse_file_locally(file_path)
        if not content:
            log_with_timestamp(f"文件解析失败: {filename}")
            return 'unknown'
        
        content_lower = content.lower()
        
        # 关键词匹配规则
        contract_keywords = [
            '合同', 'contract', '甲方', '乙方', '合同条款', '合同金额', 
            '合同期限', '合同内容', '双方权利义务', '违约责任', '合同签署'
        ]
        
        tender_keywords = [
            '招标文件', 'tender', '招标', '招标文件', '招标公告', '招标要求',
            '技术规格', '商务条款', '评标标准', '投标截止', '开标时间'
        ]
        
        bid_keywords = [
            '投标', 'bid', '投标文件', '投标报价', '技术方案', '商务方案',
            '投标函', '投标保证金', '履约能力', '业绩证明'
        ]
        
        award_keywords = [
            '中标', '中标通知书', 'award', '中标结果', '中标公告', '中标金额',
            '中标候选人', '评标结果', '中标公示'
        ]
        
        # 计算关键词匹配分数
        contract_score = sum(1 for keyword in contract_keywords if keyword in content_lower)
        tender_score = sum(1 for keyword in tender_keywords if keyword in content_lower)
        bid_score = sum(1 for keyword in bid_keywords if keyword in content_lower)
        award_score = sum(1 for keyword in award_keywords if keyword in content_lower)
        
        # 判断文件类型
        scores = {
            'contract': contract_score,
            'tender': tender_score,
            'bid': bid_score,
            'award': award_score
        }
        
        # 找到最高分且超过阈值的类型
        max_score = max(scores.values())
        if max_score >= 2:  # 设置阈值
            detected_type = max(scores, key=scores.get)
            log_with_timestamp(f"备用方法检测到文件类型: {detected_type} (分数: {max_score})")
            return detected_type
        
        log_with_timestamp(f"备用方法无法确定文件类型: {filename}")
        return 'unknown'
        
    except Exception as e:
        log_with_timestamp(f"备用文件类型检测出错 {filename}: {e}")
        return 'unknown'

def validate_file_position(file_type, expected_type, filename=""):
    """
    验证文件位置是否符合要求
    
    Args:
        file_type: 检测到的文件类型
        expected_type: 期望的文件类型
        filename: 文件名
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if file_type == 'unknown':
        return False, f"文件 '{filename}' 类型无法确定，请检查文件内容"
    
    if file_type != expected_type:
        error_messages = {
            'contract': '此文件似乎是合同文件',
            'tender': '此文件似乎是招标文件',
            'bid': '此文件似乎是投标文件', 
            'award': '此文件似乎是中标通知书'
        }
        
        expected_names = {
            'contract': '合同',
            'tender': '招标文件',
            'bid': '投标文件',
            'award': '中标通知书'
        }
        
        expected_name = expected_names.get(expected_type, expected_type)
        detected_name = error_messages.get(file_type, f'{file_type}类型文件')
        
        return False, f"文件位置错误：{detected_name} 放在了 {expected_name} 位置。请将文件放置在正确的位置。"
    
    return True, ""

def analyze_project_files(file_configs):
    """
    分析项目中的所有文件
    
    Args:
        file_configs: 文件配置列表，每个包含 {'file', 'type', 'path', 'name'}
    
    Returns:
        dict: 分析结果
    """
    results = {
        'valid_files': [],
        'invalid_files': [],
        'detected_types': {},
        'ready_for_analysis': False
    }
    
    for config in file_configs:
        detected_type = detect_file_type(config['path'], config['name'])
        config['detected_type'] = detected_type
        
        is_valid, error_msg = validate_file_position(detected_type, config['type'], config['name'])
        
        if is_valid:
            results['valid_files'].append(config)
            results['detected_types'][config['name']] = detected_type
        else:
            results['invalid_files'].append({
                'config': config,
                'error': error_msg
            })
    
    # 检查是否准备好进行分析
    contract_files = [f for f in results['valid_files'] if f['type'] == 'contract']
    results['ready_for_analysis'] = len(contract_files) > 0 and len(results['invalid_files']) == 0
    
    return results
