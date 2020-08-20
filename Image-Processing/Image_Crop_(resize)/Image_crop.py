import cv2 ##import the module
img = cv2.imread("rose.jpg") ##read your image 
y = 0  ##HEIGHT from
x = 0  ##WIDTH from
h = 300 ##HEIGHT
w = 510 ##WIDTH
crop_image = img[x:w, y:h]
cv2.imshow("Cropped", crop_image) ##display Cropped image
cv2.waitKey(0)
