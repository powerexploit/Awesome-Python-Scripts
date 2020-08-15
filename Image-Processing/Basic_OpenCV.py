##Installation

##Windows
##$ pip install opencv-python
##MacOS
##$ brew install opencv3 --with-contrib --with-python3
##Linux
##$ sudo apt-get install libopencv-dev python-opencv


##import the module i.e opencv
import cv2

##Reading Images and Finding Image details


img = cv2.imread('rose.jpg') ##imread() is function use to read image which accepts iamge path

##Image details
print("- Number of Pixels: " + str(img.size))  ## .size will show image size 
print("- Shape/Dimensions: " + str(img.shape)) ## .shape will show image shape/dimensions 
print("- Datatype: " + str(img.dtype))  ##unit8


##Dispaly Image
cv2.imshow("your image", img)
cv2.waitKey(0) ##KeyBoard Event 
