import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# flatten to black and white

def flatten_to_bw(image):
    thresh = 200
    fn = lambda x : 255 if x > thresh else 0
    try:
        return image.convert('L').point(fn, mode='1')
    except Exception as e:
        print(e)
        
def process_image(image):
    try:
        im = Image.open(image)
        print(im)
        return pytesseract.image_to_string(im)
    except Exception as e:
        print(e)
