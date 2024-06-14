import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# resize image
im = Image.open('pdfs/page0.jpg')
thresh = 200
fn = lambda x : 255 if x > thresh else 0
im = im.convert('L').point(fn, mode='1')

print(pytesseract.image_to_string(Image.open('pdfs/page0-resize.jpg')))