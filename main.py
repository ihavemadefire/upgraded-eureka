from download import download_file
from pdf_scrape import flatten_to_bw
from pdf_to_jpg import convert_pdf_to_jpg
from process import process_image

def main():
    download_file()
    print('Downloaded files!')
    convert_pdf_to_jpg('pdfs/raw/', 'pdfs/transformed/')
    print('Converted files!')
    flatten_to_bw('pdfs/transformed/', 'pdfs/flattened/')
    process_image()

if __name__ == '__main__':
    main()