import pytesseract 
from PIL import Image

# path to the Tessaract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert():
    #Image to Convert
    img = Image.open(r"img1.jpg")
    #sending Image to Pytesseract
    text = pytesseract.image_to_string(img) 
    # printing out Text from the Images\
    print(text)  
    # If you want to save the output in a file, if not comment out the next two lines
    # To open a file in write mode
    newfile = open("newfile.txt", "w+") 
    # To Write the text in that file
    newfile.write(text)
 
convert()
