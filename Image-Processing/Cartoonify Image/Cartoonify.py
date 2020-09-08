# Importing Libraries
import cv2
import numpy as np
from skimage import io

# Class Defination
class Cartoon:
    def __init__(self):
        img = io.imread("images/sunset.jpg")
        # 1) Edges Image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 7)

        # 2) Color Image
        color = cv2.bilateralFilter(img, 10, 300, 300)
        RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 3) Cartoon Image
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        cartoon_img = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)

        # Re-sizeing Image
        resize = cv2.resize(RGB_img, (600, 450))
        resize2 = cv2.resize(cartoon_img, (600, 450))
        self.resize = resize
        self.resize2 = resize2

# Displaying Image
# Creating an object of class Cartoon
c1 = Cartoon()
c1.resize
c1.resize2
cv2.imshow("Original_Image", c1.resize)
cv2.imshow("Cartoonified_Image", c1.resize2)
cv2.waitKey(0)
cv2.destroyAllWindows()
