import cv2 ##import the module
img = cv2.imread("rose.jpg") ##read your image 

cv2.imshow('Original Image', img)  ##this will display the image original image
cv2.waitKey(0)


##.shape will give you height and width of image
height, width = img.shape[0:2]
##getrotationmatrix2d will create a rotation matrix  "(center, angle, scale)" => arguments
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
## the wrapAffine function will rotate image "(img, rotationMatrix, (width, height))" => arguments
rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height)) 

cv2.imshow('Rotated Image', rotatedImage)

cv2.waitKey(0)
