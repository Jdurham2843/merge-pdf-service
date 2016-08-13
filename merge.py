import sys
import re
from PyPDF2 import PdfFileMerger

def merge(files):
    check_if_pdfs(files)
    merger = PdfFileMerger()

    for file_name in files:
        try:
            opened = open(file_name, 'rb')
        except:
            print('%s could not be opened :/' % file_name)
            raise
        else:
            merger.append(file_name)
            opened.close()

    with open('merged.pdf', 'wb') as final_file:
        merger.write(final_file)

def check_if_pdfs(files):
    pattern = '.+\.pdf'
    for file_name in files:
        if not re.match(pattern, file_name):
            raise Exception('File is not a pdf file')


if __name__ == '__main__':
    merge(sys.argv[1:])
