'''
Script uses Pillow module to read the image and convert it to png.
sys module for accepting inputs from terminal and os module 
for operations on pathnames.

Install Pillow module through "pip install pillow"
'''

import sys,os
from PIL import Image

source_folder = sys.argv[1]  # Accepts source folder given in terminal
destination_folder = sys.argv[2] # Accepts destination folder given in terminal

if not os.path.exists(destination_folder):  #Check if destination folder exists,if not creates one
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder): # For each file present in Source folder
    file = os.path.splitext(filename)[0]  # Splits file name into as tuple as ('filename','.extension')
    img = Image.open(f'{source_folder}/{filename}')
    img.save(f'{destination_folder}/{file}.png','png') #Converts to png format
    print("Image converted!")

'''
Sample input to run in terminal:
->Python3 JpgToPngConvertor.py Source_Images Destination_Images

Output:
Images in Source_Images folder will be converted into Png Images and gets stored in
Destination_Images folder
'''

