import cv2 ##import the module opencv
import numpy as np ##import the module numpy
import pyzbar.pyzbar as pyzbar ##import the module pyzbar

img = cv2.imread("qr.png") ##read your image 
decode_QR = pyzbar.decode(img) ##function to decode QR

for i in decode_QR:
	print("your scanned QR :",i.data)

cv2.imshow("QR ", img) ##display Cropped image
cv2.waitKey(0)
