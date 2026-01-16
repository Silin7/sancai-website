import os
import hashlib
from datetime import datetime
from flask import current_app, session
from app.utils import log_with_timestamp, push_sse_event
from app.data_storage.file_metadata import (
    save_upload_file,
    load_md5_mapping,
    convert_doc_file,
    update_md5_entry
)
from app.config import Config


def ensure_file_converted(file_path, file_md5, original_filename, project_id=None, user_id=None, file_type=None):
    """
    确保文件已经过必要的转换（DOC→DOCX, 图片PDF→OCR DOCX）

    这是一个公共函数，被 process_single_file() 和 validate_file_by_md5() 调用。

    Args:
        file_path: 文件路径
        file_md5: 文件 MD5
        original_filename: 原始文件名
        project_id: 项目ID（用于OCR状态追踪）
        project_id: 项目ID（用于OCR状态追踪）
        user_id: 用户ID（用于OCR状态追踪和SSE推送）
        file_type: 文档类型（用于选择OCR模型）

    Returns:
        dict: {
            'path': 最终文件路径,
            'md5': 最终文件 MD5,
            'display_name': 显示文件名,
            'converted': 是否进行了转换,
            'conversion_type': 转换类型（'doc_to_docx' / 'pdf_ocr' / None）,
            'original_md5': 原始文件 MD5（如果转换过）
        }
    """
    file_ext = os.path.splitext(file_path)[1].lower()

    # 记录原始信息
    original_md5_value = file_md5
    converted = False
    conversion_type = None
    final_path = file_path
    final_md5 = file_md5
    original_display_name = original_filename  # ✅ 使用原始文件名
    converted_name = None  # 🆕 转换后的文件名
    
    # 🆕 如果没有传递user_id，尝试从session获取
    if not user_id:
        user_id = session.get('user_id', 'default_user')

    # 首先检查 MD5 映射，看看是否已经转换过
    md5_mapping = load_md5_mapping()
    entry = md5_mapping.get(file_md5)
    if entry and entry.get('converted_to'):
        # 已经转换过，直接返回转换后的文件信息
        converted_md5 = entry.get('converted_to')
        converted_entry = md5_mapping.get(converted_md5)
        if converted_entry and converted_entry.get('filename'):
            converted_path = os.path.join(
                current_app.config['UPLOAD_FOLDER'],
                converted_entry['filename']
            )
            if os.path.exists(converted_path):
                log_with_timestamp(f"✅ 发现已转换文件，直接使用: {converted_entry['filename']}")
                return {
                    'path': converted_path,
                    'md5': converted_md5,
                    'display_name': original_filename,  # ✅ 原始文件名
                    'converted_name': converted_entry['filename'],  # ✅ 转换后的文件名
                    'converted': True,
                    'conversion_type': entry.get('conversion_type'),
                    'original_md5': file_md5
                }

    # 处理 DOC 文件转换
    if file_ext == '.doc':
        log_with_timestamp(f"检测到DOC文件，开始转换: {original_filename}")
        try:
            docx_path, docx_md5, docx_name = convert_doc_file(file_path, file_md5, original_filename)

            # 更新返回信息为转换后的文件
            final_path = docx_path
            final_md5 = docx_md5
            converted_name = docx_name  #  转换后的文件名
            converted = True
            conversion_type = 'doc_to_docx'

            log_with_timestamp(f"DOC转换成功: {original_filename} → {docx_name}")

        except Exception as conv_error:
            log_with_timestamp(f"DOC转换失败 {original_filename}: {conv_error}")
            # 转换失败时，继续使用原始文件
            converted = False

    # 处理图片 PDF（OCR 转换）-  同步执行 + SSE进度推送
    elif file_ext == '.pdf':
        try:
            # 使用智能PDF类型检测工具
            from app.pipeline.preprocess.pdf_type_detector import is_image_based_pdf
            
            detection_result = is_image_based_pdf(file_path)

            if detection_result['is_image_pdf']:
                log_with_timestamp(
                    f"检测到图片型PDF: {original_filename}\n"
                    f"  - 置信度: {detection_result['confidence']:.2%}\n"
                    f"  - 判断理由: {detection_result['reason']}"
                )

                # 🆕 立即推送OCR检测事件
                if user_id:
                    push_sse_event(user_id, 'ocr_detected', {
                        'filename': original_filename,
                        'message': f'检测到图片型PDF "{original_filename}"，开始OCR转换...'
                    })
                
                    # 🆕 设置OCR处理状态（用于页面刷新恢复）
                    if project_id and file_md5:
                        from app.data_storage.file_metadata import set_file_ocr_status
                        set_file_ocr_status(
                            user_id, project_id, file_md5, original_filename,
                            status='converting', progress=0, message='OCR转换中...'
                        )

                from app.pipeline.preprocess.pdf_ocr_processor import process_image_pdf_ocr_and_docx

                # 🆕 同步执行OCR转换（会通过SSE推送进度）
                ocr_text, ocr_info = process_image_pdf_ocr_and_docx(
                    file_path,
                    original_filename,
                    generate_docx=True,
                    user_id=user_id,  # 🆕 传递user_id用于SSE推送
                    project_id=project_id,  # 🆕 传递project_id用于状态持久化
                    doc_type=file_type  # 🆕 传递文档类型给OCR处理器
                )

                if ocr_text and ocr_info.get('docx_path'):
                    docx_path = ocr_info['docx_path']
                    docx_md5 = ocr_info.get('docx_md5')
                    docx_name = os.path.basename(docx_path)

                    # 如果没有 docx_md5，计算一下
                    if not docx_md5 and os.path.exists(docx_path):
                        with open(docx_path, 'rb') as f:
                            docx_md5 = hashlib.md5(f.read()).hexdigest()

                    # 更新 MD5 映射
                    if docx_md5:
                        update_md5_entry(docx_md5, {
                            'filename': docx_name,
                            'upload_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'file_size': os.path.getsize(docx_path),
                            'converted_from': original_md5_value,
                            'conversion_type': 'pdf_ocr'
                        })

                        update_md5_entry(original_md5_value, {
                            'converted_to': docx_md5,
                            'conversion_type': 'pdf_ocr'
                        })

                    # 更新返回信息为转换后的文件
                    final_path = docx_path
                    final_md5 = docx_md5 or file_md5
                    converted_name = docx_name  # 🆕 转换后的文件名
                    converted = True
                    conversion_type = 'pdf_ocr'

                    log_with_timestamp(f"✅ 图片PDF OCR转换成功: {original_filename} → {docx_name}")
                    
                    # 🆕 清除OCR处理状态
                    if project_id and file_md5:
                        from app.data_storage.file_metadata import clear_file_ocr_status
                        clear_file_ocr_status(user_id, project_id, file_md5)
                
                # 🆕 检查是否被取消
                elif ocr_info.get('cancelled'):
                    log_with_timestamp(f"🛑 图片PDF OCR已取消: {original_filename}")
                    return {
                        'path': file_path,
                        'md5': file_md5,
                        'display_name': original_filename,
                        'converted': False,
                        'cancelled': True  # 标记已取消
                    }
                
                else:
                    log_with_timestamp(f"⚠️ 图片PDF OCR未生成DOCX，使用原始文件: {original_filename}")
                    # 🆕 清除OCR处理状态
                    if project_id and file_md5:
                        from app.data_storage.file_metadata import clear_file_ocr_status
                        clear_file_ocr_status(user_id, project_id, file_md5)

        except Exception as pdf_error:
            log_with_timestamp(f"❌ PDF处理失败 {original_filename}: {pdf_error}")
            # PDF 处理失败时，继续使用原始文件
            converted = False

    # 构建返回结果
    result = {
        'path': final_path,
        'md5': final_md5,
        'display_name': original_display_name,  # ✅ 始终返回原始文件名作为显示名
        'converted_name': converted_name,  # 🆕 转换后的文件名
        'converted': converted,
        'conversion_type': conversion_type
    }

    # 如果转换过，记录原始 MD5 和转换后文件的 MD5
    if converted:
        result['original_md5'] = original_md5_value
        result['converted_file_md5'] = final_md5  # 🆕 返回转换后文件的MD5

    return result


def process_single_file(file_storage, original_filename, expected_type, project_id=None, user_id=None):
    """
    处理单个文件 - 保存文件并进行必要的转换
    - 保存到 uploads/ 目录
    - DOC 文件自动转换为 DOCX
    - 图片 PDF 自动进行 OCR 处理并生成 DOCX
    - 更新 MD5 映射

    Args:
        file_storage: 文件对象
        original_filename: 原始文件名
        expected_type: 期望的文件类型
        project_id: 项目ID（用于OCR状态追踪）
        user_id: 用户ID（用于OCR状态追踪和SSE推送）

    Returns:
        dict: {
            'success': True/False,
            'path': 最终文件路径,
            'md5': 最终文件 MD5（转换后的或原始的）,
            'name': 原始文件名,
            'display_name': 显示文件名,
            'converted_name': 转换后文件名（如果转换过）,
            'type': 文件类型,
            'converted': 是否进行了转换,
            'conversion_type': 转换类型（'doc_to_docx' / 'pdf_ocr' / None）,
            'original_md5': 原始文件 MD5（如果转换过）
        }
    """
    try:
        # 1. 保存原始文件到 uploads/
        file_path, filename, file_md5 = save_upload_file(file_storage, original_filename)

        # 2. 使用公共函数处理文件转换（🆕 传递project_id和user_id用于OCR状态追踪）
        conversion_result = ensure_file_converted(file_path, file_md5, original_filename, project_id, user_id, file_type=expected_type)

        # 3. 构建返回结果
        result = {
            'success': True,
            'path': conversion_result['path'],
            'md5': conversion_result['md5'],
            'name': original_filename,
            'display_name': conversion_result['display_name'],
            'converted_name': conversion_result.get('converted_name', original_filename),
            'type': expected_type,
            'converted': conversion_result['converted'],
            'conversion_type': conversion_result.get('conversion_type')
        }

        # 如果转换过，记录原始 MD5、转换后文件 MD5 和路径
        if conversion_result['converted']:
            result['original_md5'] = conversion_result.get('original_md5')
            result['converted_file_md5'] = conversion_result.get('converted_file_md5')  # 🆕 返回转换后文件MD5
            result['original_path'] = file_path

        return result

    except Exception as e:
        log_with_timestamp(f"文件处理失败 {original_filename}: {e}")
        return {
            'success': False,
            'error': str(e)
        }

def check_file_reuse(md5):
    """检查文件是否可以重复使用"""
    # 使用project_file_manager中的load_md5_mapping
    md5_mapping = load_md5_mapping()
    entry = md5_mapping.get(md5)
    if entry:
        stored_filename = entry.get('stored_filename')
        if stored_filename:
            from flask import current_app
            path = os.path.join(current_app.config['UPLOAD_FOLDER'], stored_filename)
            if os.path.exists(path):
                return {'path': path}
    return None
