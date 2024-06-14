import urllib.request


urls = ['https://www.mummesinc.com/s/PRESS_flyer_DeerCornpdf.pdf',
        'https://www.mummesinc.com/s/PRESS_flyer_20DeerPellets.pdf',
        'https://www.mummesinc.com/s/PRESS_flyer_16DeerPellets.pdf',
        'https://www.mummesinc.com/s/PRESS_flyer_ProMax.pdf'
        ]
for url in urls:
    file_path = '/Users/Jacob_Ide/mummes/pdfs/raw/{}'.format(url.split('/')[-1])
    urllib.request.urlretrieve(url, file_path)
    print("File downloaded successfully!")
