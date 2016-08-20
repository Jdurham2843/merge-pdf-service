import sys
import os
import re
from PyPDF2 import PdfFileMerger

def merge(files):
    merger = PdfFileMerger()

    for file_name in files:
        try:
            opened = open('uploads/%s' % (file_name), 'rb')
        except:
            raise Exception('uploads/%s' % (file_name))
        else:
            merger.append(opened)

    with open('uploads/merged.pdf', 'wb') as final_file:
        merger.write(final_file)

    cleanup_uploads_folder(files)

def cleanup_uploads_folder(files):
        """ This function cleanups up the uploads folder"""
        for filename in files:
                os.remove('uploads/%s' % filename)

def format_files(files):
    delim = {' ', '(', ')', '{', '}', '[', ']'}
    files_formatted = []
    for file_name in files:
        file_name_formatted = []
        for char in file_name:
            if char not in delim:
                file_name_formatted.append(char)
            elif char == ' ':
                file_name_formatted.append('_')
        file_name_formatted_str = ''.join(file_name_formatted)
        files_formatted.append(file_name_formatted_str)
    return files_formatted

if __name__ == '__main__':
    merge(sys.argv[1:])
