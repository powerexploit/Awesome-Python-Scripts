
#import the recessary libraries
import cv2
import pytesseract
import pdf2image as pdf

#define some pdf to image exception (optional)
from pdf2image.exceptions import (
PDFInfoNotInstalledError,
PDFPageCountError,
PDFSyntaxError
)

#specify the tesseract exe file location
pytesseract.pytesseract.tesseract_cmd = '<-------------------exe-location--------------------->\tesseract.exe'

# specify the PDF file path
file_path='<-------------------------your pdf file path--------------------------->'

def pdf2text(file_path):
    """
    :param file_path: the location of your pdf file
    :return: return none
    :concept: it will convert your pdf file to image and image to text, and store the image and txt file in the same location
    """
    
    #convert the pdf file to image file, here you have to specify the poppler's bin folder path
    images = pdf.convert_from_path(file_path, 500, poppler_path='<-------------poppler-folder-path-------------------->\poppler-0.68.0\bin')

    #set the image count to 1
    image_count = 1

    #iterate over each page in the pdf
    for image in images:

        #this will be the stored image name
        image_name = "page" + str(image_count) + ".jpeg"

        #store the image in the same location
        image.save(image_name, 'JPEG')

        #read the stored image as gray scale
        img = cv2.imread(image_name, 1)

        #show the read image
        cv2.imshow('image', img)

        #convert the image to text and store it in a variable
        text = pytesseract.image_to_string(img)
        print(text)

        #define the text file name
        text_count = 1
        text_file = "text" + str(text_count) + ".txt"

        #open the text file and write the read text init
        with open(text_file, 'w+') as f:
            f.writelines(text)

        #increase the counter to process each page of the PDF file
        text_count += 1
        image_count += 1
    cv2.waitKey(0)


