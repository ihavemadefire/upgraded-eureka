import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# flatten to black and white

src='pdfs/flattened/'

def process_image(src=src):
    print('Processing images...')
    print(os.listdir('pdfs/flattened/'))
    for file in os.listdir('pdfs/flattened/'):
        try:
            im = Image.open(src + file)
            print(pytesseract.image_to_string(im))
            return pytesseract.image_to_string(im)
        except Exception as e:
            print(e)