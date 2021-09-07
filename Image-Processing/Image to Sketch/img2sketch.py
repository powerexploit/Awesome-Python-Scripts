import cv2
import numpy as np

img= cv2.imread('tiger.png', -1)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

inverted= 255-grayscale
blurred= cv2.blur(inverted,(15,15)) 

def dodge(front,back): 
    result=front*255/(255-back)  
    result[result>255]=255 
    result[back==255]=255 
    return result.astype('uint8')

blurred= blurred.astype('float')
grayscale= grayscale.astype('float')
final_img= dodge(blurred, grayscale)

cv2.imwrite('sketch.jpg',final_img)



