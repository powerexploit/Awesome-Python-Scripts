import os
import qrcode
from sys import argv
from urllib.parse import urlparse
import random

if len(argv)==2:
	url =  str(argv[1])
else:
	url = input("Enter an URL to Encode in QR: ")

path = ((urlparse(url)).netloc)
image = qrcode.make(url) 

if os.path.exists(f"{path}.png"):
	path = path + str(random.randint(0,10000))

image.save(f"{path}.png", "PNG")
file_path = os.path.abspath(path)
print("File saved to:", file_path)