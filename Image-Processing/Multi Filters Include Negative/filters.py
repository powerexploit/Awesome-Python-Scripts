from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
import negative_image
import cv2
import sys
import os

# Loading images
if len(sys.argv) == 2:
	fn_with_ext = sys.argv[1]
	filename, file_extension = os.path.splitext(sys.argv[1])
else:
    print("No input image given, so loading default image, lena.jpg \n")
    print("Correct Usage: python grabcut.py <filename> \n")  

# Insert path here 
img = Image.open(fn_with_ext)
img = img.convert('RGB')

plt.imshow(img)
plt.show()

# List of Filters (is selected in menu option)
filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS, ImageFilter.FIND_EDGES, ImageFilter.SHARPEN, ImageFilter.SMOOTH, ImageFilter.SMOOTH_MORE]
 
while True:
	try:
		print("MENU OF FILTERS IMAGE APPLICATION", end=" ")
		print("(CHOOSE A OPTION BELLOW TO FILTER AN IMAGE):")

		print("1- BLUR")
		print("2- CONTOUR")
		print("3- DETAIL")
		print("4- EDGE_ENHANCE")
		print("5- EDGE_ENHANCE_MORE")
		print("6- EMBOSS")
		print("7- FIND_EDGES")
		print("8- SHARPEN")
		print("9- SMOOTH")
		print("10- SMOOTH_MORE")
		print("11- NEGATIVE")
		print("Ctr+D FOR EXIT")

		opt = None
		while True:
			try:
				opt = int(input())
				if (opt >= 1 and opt <= 11):
					break
			except ValueError:
				print("PLEASE, DIGIT A INTEGER NUMBER BETWEEN 1 AND 11")

		if (opt >= 1 and opt <= 10):
			img1 = img.filter(filters[opt-1])
			img1.save(f"./images/{filename}_{opt}_converted{file_extension}", "JPEG")
		else:
			img1 = negative_image.negative(fn_with_ext)
			cv2.imwrite(f"./images/{filename}_{opt}_converted{file_extension}", img1)

		plt.imshow(img1)
		plt.show()
	except EOFError:
		break