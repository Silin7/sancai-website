# app/pipeline/preprocess/file_parser.py
# 文件解析和转换工具
import os
import subprocess
from datetime import datetime
from ...utils import log_with_timestamp


def parse_file_locally(file_path, enable_ocr=False):
    """
    本地解析文件内容（仅解析已转换的文字型文件）

    Args:
        file_path: 文件路径（应该是已转换的DOCX或文字型PDF）
        enable_ocr: 保留参数以向后兼容，但默认为False（转换应在上传校验阶段完成）

    Returns:
        str: 解析后的文本内容
    """
    from ...config import Config
    if not Config.LOCAL_LIBS_INSTALLED:
        raise Exception("本地解析库未安装")
    import fitz
    import docx
    ext = os.path.splitext(file_path)[1].lower()
    original_filename = os.path.basename(file_path)

    try:
        if ext == '.pdf':
            # 🆕 使用智能PDF类型检测工具
            from .pdf_type_detector import is_image_based_pdf
            
            detection_result = is_image_based_pdf(file_path)
            
            if detection_result['is_image_pdf']:
                # 图片PDF应该在上传校验阶段已经转换为DOCX
                # 如果走到这里，说明校验阶段没有正确处理
                log_with_timestamp(
                    f"错误：图片PDF应在上传校验阶段转换，但未转换: {original_filename}\n"
                    f"  - {detection_result['reason']}"
                )
                raise ValueError(f"图片版PDF未经OCR转换，请重新上传")
            
            # 提取文本内容
            doc = fitz.open(file_path)
            content = "".join([page.get_text() for page in doc])
            return content
        elif ext == '.docx':
            doc = docx.Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        log_with_timestamp(f"本地解析失败 ({file_path}): {e}")
        raise e
    return None

def parse_file_locally2(file_path, enable_ocr=False):
    """
    本地解析文件内容（仅解析已转换的文字型文件）
    支持提取Word文档中的段落和表格
    
    Args:
        file_path: 文件路径（应该是已转换的DOCX或文字型PDF）
        enable_ocr: 保留参数以向后兼容，但默认为False（转换应在上传校验阶段完成）
        
    Returns:
        str: 解析后的文本内容
    """
    from ...config import Config
    if not Config.LOCAL_LIBS_INSTALLED:
        raise Exception("本地解析库未安装")
    import fitz
    import docx
    ext = os.path.splitext(file_path)[1].lower()
    original_filename = os.path.basename(file_path)
    
    try:
        if ext == '.pdf':
            # 🆕 使用智能PDF类型检测工具
            from .pdf_type_detector import is_image_based_pdf
            
            detection_result = is_image_based_pdf(file_path)
            
            if detection_result['is_image_pdf']:
                # 图片PDF应该在上传校验阶段已经转换为DOCX
                # 如果走到这里，说明校验阶段没有正确处理
                log_with_timestamp(
                    f"错误：图片PDF应在上传校验阶段转换，但未转换: {original_filename}\n"
                    f"  - {detection_result['reason']}"
                )
                raise ValueError(f"图片版PDF未经OCR转换，请重新上传")
            
            # 提取文本内容
            doc = fitz.open(file_path)
            content = "".join([page.get_text() for page in doc])
            return content
            
        elif ext == '.docx':
            doc = docx.Document(file_path)
            # 按文档顺序提取段落和表格
            return extract_docx_with_tables(doc)
            
    except Exception as e:
        log_with_timestamp(f"本地解析失败 ({file_path}): {e}")
        raise e
    return None


def extract_docx_with_tables(doc):
    """
    按文档顺序提取Word文档中的段落和表格内容
    """
    full_text = []
    
    # 遍历文档的所有body元素
    for element in doc.element.body:
        # 处理段落
        if element.tag.endswith('p'):
            # 提取段落文本，过滤None值
            text = ''.join(
                node.text for node in element.iter() 
                if hasattr(node, 'text') and node.text is not None
            )
            if text.strip():
                full_text.append(text)
        
        # 处理表格
        elif element.tag.endswith('tbl'):
            # 找到对应的表格对象
            for table in doc.tables:
                if table._element == element:
                    # 提取表格内容
                    table_text = extract_table_content(table)
                    if table_text:
                        full_text.append(table_text)
                    break
    
    return '\n'.join(full_text)


def extract_table_content(table):
    """
    提取表格内容为格式化文本
    
    Args:
        table: docx.table.Table对象
        
    Returns:
        str: 格式化的表格文本（使用制表符分隔列）
    """
    rows_text = []
    
    for row in table.rows:
        cells_text = []
        for cell in row.cells:
            cell_text = cell.text.strip()
            # 清理单元格内的多余空白
            cell_text = ' '.join(cell_text.split())
            cells_text.append(cell_text)
        
        # 使用制表符连接单元格
        row_text = '\t'.join(cells_text)
        if row_text.strip():
            rows_text.append(row_text)
    
    return '\n'.join(rows_text)

def convert_doc_to_docx(doc_path):
    """
    使用 LibreOffice 将 .doc 转换为 .docx,通过 txt 中间格式保留编号。
    转换链: .doc → .txt → .docx
    返回新的 .docx 文件的路径。
    """
    log_with_timestamp(f"开始将 {doc_path} 转换为 .docx (通过txt中间格式)...")
    output_dir = os.path.dirname(doc_path)
    base_name = os.path.splitext(os.path.basename(doc_path))[0]
    
    # 确定命令前缀
    soffice_cmd = 'soffice.com' if os.name == 'nt' else 'soffice'
    
    try:
        # 第一步: doc → txt
        log_with_timestamp(f"步骤1: 转换 {doc_path} 为 .txt...")
        txt_path = os.path.join(output_dir, f"{base_name}.txt")
        
        command_txt = [
            soffice_cmd, 
            '--headless', 
            '--convert-to', 
            'txt:Text (encoded):UTF8',  # 指定UTF-8编码
            '--outdir', 
            output_dir, 
            doc_path
        ]
        
        result = subprocess.run(
            command_txt, 
            check=True, 
            capture_output=True, 
            text=True, 
            timeout=600
        )
        log_with_timestamp(f"txt转换完成: {result.stdout}")
        
        if not os.path.exists(txt_path):
            raise FileNotFoundError(f"txt文件未生成: {txt_path}")
        
        # 第二步: txt → docx
        log_with_timestamp(f"步骤2: 转换 {txt_path} 为 .docx...")
        docx_path = os.path.join(output_dir, f"{base_name}.docx")
        
        command_docx = [
            soffice_cmd,
            '--headless',
            '--convert-to',
            'docx',
            '--outdir',
            output_dir,
            txt_path
        ]
        
        result = subprocess.run(
            command_docx,
            check=True,
            capture_output=True,
            text=True,
            timeout=600
        )
        log_with_timestamp(f"docx转换完成: {result.stdout}")
        
        if not os.path.exists(docx_path):
            raise FileNotFoundError(f"docx文件未生成: {docx_path}")
        
        # 清理中间文件(可选)

        while os.path.exists(txt_path):
            import time
            os.remove(txt_path)
            time.sleep(0.51)
        log_with_timestamp(f"已删除中间文件: {txt_path}")
        
        log_with_timestamp(f"文件成功转换为: {docx_path}")
        return docx_path
        
    except subprocess.TimeoutExpired:
        log_with_timestamp(f"转换超时: {doc_path}")
        raise
    except subprocess.CalledProcessError as e:
        log_with_timestamp(f"转换失败: {e.stderr}")
        raise
    except Exception as e:
        log_with_timestamp(f"转换过程出错: {str(e)}")
        raise

    except FileNotFoundError:
        log_with_timestamp("错误: 'soffice' 命令未找到。请确保 LibreOffice 已安装并添加到系统 PATH。")
        raise Exception("'soffice' command not found. LibreOffice might not be installed.")
    except subprocess.CalledProcessError as e:
        log_with_timestamp(f"LibreOffice 转换失败。 Stderr: {e.stderr}")
        raise Exception(f"DOC to DOCX conversion failed: {e.stderr}")
    except subprocess.TimeoutExpired:
        log_with_timestamp("LibreOffice 转换超时。")
        raise Exception("DOC to DOCX conversion timed out.")
    except Exception as e:
        log_with_timestamp(f"转换过程中发生未知错误: {e}")
        raise e
    

def convert_doc_to_pdf(doc_path):
    """
    使用 LibreOffice 将 .doc 文件转换为 .pdf
    返回新的 .pdf 文件的路径。
    """
    log_with_timestamp(f"开始将 {doc_path} 转换为 .pdf...")
    output_dir = os.path.dirname(doc_path)
    base_name = os.path.splitext(os.path.basename(doc_path))[0]
    soffice_cmd = 'soffice.com' if os.name == 'nt' else 'soffice'
    
    try:
        command = [
            soffice_cmd,
            '--headless',
            '--convert-to',
            'pdf',
            '--outdir',
            output_dir,
            doc_path
        ]
        
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        log_with_timestamp(f"PDF转换完成: {result.stdout}")
        
        pdf_path = os.path.join(output_dir, f"{base_name}.pdf")
        if os.path.exists(pdf_path):
            log_with_timestamp(f"文件成功转换为: {pdf_path}")
            return pdf_path
        else:
            raise FileNotFoundError("转换后的 .pdf 文件未在预期位置找到。")
            
    except subprocess.TimeoutExpired:
        log_with_timestamp(f"转换超时: {doc_path}")
        raise
    except subprocess.CalledProcessError as e:
        log_with_timestamp(f"转换失败: {e.stderr}")
        raise


