from PIL import Image
import pytesseract
import cv2
import os

# path to the Tessaract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("image.jpg")                                            #read image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                             #convert image into gray colored image
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)                                                #write image into file
text = pytesseract.image_to_string(Image.open(filename))                   #convert image into string and store in variable text
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(1)
print("successfully found") if 'NEVER' in text else print("Text Not Found")
os.remove(filename)

