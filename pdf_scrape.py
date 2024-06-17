import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# flatten to black and white
src = 'pdfs/transformed/'
dest = 'pdfs/flattened/'
def flatten_to_bw(src=src, dest=dest):
    print('Flattening images to black and white...')
    thresh = 200
    fn = lambda x : 255 if x > thresh else 0
    for file in os.listdir(src):
        
        try:
            im = Image.open(src + file)
            im = im.convert('L').point(fn, mode='1')
            im.save(dest + file)
        except Exception as e:
            print(e)
            continue

