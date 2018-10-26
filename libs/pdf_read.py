from libs.trans_text import *
from libs.speech import *
import PyPDF2
import cv2


def pdf_read(file,lang_dest,lang_source,translate):
    # creating a pdf file object
    pdfFileObj = open(file, 'r+b')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # getting number of pages
    num_pages = pdfReader.numPages
    print("There are %i pages",num_pages)
    start_page = int(input("Start from page: "))-1

    for i in range(start_page,num_pages):
        # creating a page object
        pageObj = pdfReader.getPage(i)
        print (i)

        # extracting text from page
        text_string = pageObj.extractText()
        print(text_string)

        # Translates the text if translation is activated
        if translate == 'y':
            text_string = trans_text(text_string, lang_dest, lang_source)
        speech(text_string, lang_dest)
        key = 's'
        while((key != 'y')and(key != 'n')):
            key = input("Do you want to continue? y/n: ")
        if key == 'y':
            page = ("Page %i",i+1)
            speech(page,'en')
        elif key == 'n':
            break
    # closing the pdf file object
    pdfFileObj.close()
    return