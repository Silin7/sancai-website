# app/pipeline/preprocess/__init__.py
# 预处理阶段模块 - 从 contracts_handler/pre_handle_file 迁移

from .file_validator import (
    allowed_file,
    calculate_md5,
    validate_file_integrity,
)

from .file_namer import (
    get_unique_filename,
    generate_contract_id,
    generate_result_filename,
)

from .file_parser import (
    parse_file_locally,
    parse_file_locally2,
    extract_docx_with_tables,
    extract_table_content,
    convert_doc_to_docx,
)

from .file_type_detector import (
    detect_file_type,
    detect_file_type_ai,
    detect_file_type_fallback,
    validate_file_position,
    analyze_project_files,
)

from .file_page_counter import (
    get_file_page_count,
    get_pdf_page_count,
    get_docx_page_count,
)

from .image_preprocessor import (
    ImagePreprocessor,
    detect_seal_color,
    preprocess_for_ocr,
)

from .ocr_api_client import (
    DashScopeOCRClient,
    call_dashscope_ocr,
)

from .pdf_ocr_processor import PDFOCRProcessor
