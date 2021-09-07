import cv2 

def negative(image):
	img_bgr = cv2.imread(image, 1) 
	  
	img_neg = 255 - img_bgr 

	return img_neg