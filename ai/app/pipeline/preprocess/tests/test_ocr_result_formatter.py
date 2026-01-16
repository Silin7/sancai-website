import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))

from app.pipeline.preprocess.pdf_ocr_processor import (
    PDFOCRProcessor, 
    process_image_pdf_ocr, 
    process_image_pdf_ocr_and_docx
)

class TestOCRResultFormatter(unittest.TestCase):
    def setUp(self):
        self.processor = PDFOCRProcessor()
        
    def test_format_ocr_result_failure(self):
        result = {'success': False, 'error': 'Test Error'}
        text, info = self.processor._format_ocr_result(result)
        self.assertEqual(text, "")
        self.assertEqual(info['error'], 'Test Error')

    def test_format_ocr_result_success_basic(self):
        result = {
            'success': True,
            'result': {
                'combined_text': 'Hello World',
                'total_pages': 1,
                'file_md5': 'abc',
                'extraction_time': '1s'
            }
        }
        text, info = self.processor._format_ocr_result(result, include_docx_info=False)
        self.assertEqual(text, 'Hello World')
        self.assertEqual(info['total_pages'], 1)
        self.assertNotIn('docx_generated', info)

    def test_format_ocr_result_success_docx(self):
        result = {
            'success': True,
            'result': {
                'combined_text': 'Hello World',
                'docx_info': {
                    'docx_generated': True,
                    'merged_file': '/tmp/test.docx'
                }
            },
            'docx_exists': True
        }
        text, info = self.processor._format_ocr_result(result, include_docx_info=True)
        self.assertEqual(text, 'Hello World')
        self.assertTrue(info['docx_generated'])
        self.assertEqual(info['docx_path'], '/tmp/test.docx')

    @patch('app.pipeline.preprocess.pdf_ocr_processor.PDFOCRProcessor.process_pdf_with_ocr')
    def test_process_image_pdf_ocr(self, mock_process):
        mock_process.return_value = {
            'success': True,
            'result': {'combined_text': 'OCR Text', 'total_pages': 5}
        }
        text, info = process_image_pdf_ocr('dummy.pdf')
        self.assertEqual(text, 'OCR Text')
        self.assertEqual(info['total_pages'], 5)
        self.assertNotIn('docx_generated', info)

    @patch('app.pipeline.preprocess.pdf_ocr_processor.PDFOCRProcessor.process_pdf_with_ocr_and_docx')
    def test_process_image_pdf_ocr_and_docx(self, mock_process):
        mock_process.return_value = {
            'success': True,
            'result': {
                'combined_text': 'OCR Docx', 
                'docx_info': {'docx_generated': True, 'merged_file': 'path.docx'}
            },
            'docx_exists': True
        }
        text, info = process_image_pdf_ocr_and_docx('dummy.pdf')
        self.assertEqual(text, 'OCR Docx')
        self.assertTrue(info['docx_generated'])
        self.assertEqual(info['docx_path'], 'path.docx')

if __name__ == '__main__':
    unittest.main()
