# import module
from pdf2image import convert_from_path
import os
 

# Store Pdf with convert_from_path function
def convert_pdf_to_jpg(source_path, dest_path):
    # Iterate through all the pages stored above
  for file in os.listdir(source_path):
    images = convert_from_path(source_path + file)
    print('Converting {} to jpg...'.format(file))
    for i in range(len(images)):
      images[i].save('{}{}_{}.jpg'.format(dest_path, file, str(i)), 'JPEG')

