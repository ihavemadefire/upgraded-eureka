from download import download_file
from pdf_to_jpg import convert_pdf_to_jpg
import unittest
import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

class TestDownload(unittest.TestCase):

    def test_download_file(self):
        urls = ['https://github.com/ihavemadefire/upgraded-eureka/blob/main/example_pdf.pdf']
        dest = 'pdfs/raw/'
        download_file(urls, dest)
        self.assertTrue(os.path.exists('pdfs/raw/example_pdf.pdf'))
        os.remove('pdfs/raw/example_pdf.pdf')


class TestConversion(unittest.TestCase):

    def test_convert_pdf_to_jpg(self):
        images = 'test/pdfs/raw/'
        dest = 'test/pdfs/transformed/'
        convert_pdf_to_jpg(images, dest)
        self.assertTrue(os.path.exists('test/pdfs/transformed/example_pdf_0.jpg'))
        os.remove('test/pdfs/transformed/example_pdf_0.jpg')



if __name__ == '__main__':
    unittest.main()