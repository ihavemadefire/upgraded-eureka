import urllib.request

urls = ['https://file-examples.com/storage/feb74b6436666ff3195b073/2017/10/file-sample_150kB.pdf']
dest = 'pdfs/raw/'
def download_file(urls=urls, dest=dest):
    for url in urls:
        file_path = '{}{}'.format(dest, url.split('/')[-1])
        try:
            urllib.request.urlretrieve(url, file_path)
            print("{} downloaded successfully!".format(url.split('/')[-1]))
        except Exception as e:
            print("Error downloading {}: {}".format(url.split('/')[-1], e))
