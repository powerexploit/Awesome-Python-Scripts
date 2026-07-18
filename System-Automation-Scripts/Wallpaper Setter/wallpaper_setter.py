import ctypes
import os
import argparse
import sys

# Code to add the cli
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--jpgfile", required=True, help="JPG File")
args = vars(parser.parse_args())


#Storing the absolute path of the jpg file provided by the user
filename = args['jpgfile']

# To make sure a jpg file has been provided
if filename.endswith(".jpg"):
    


    # Code to get the absolute path of the jpg file
    def getabsolutepath(filename):
        path = os.path.abspath(filename)
        return path

    #The code for setting wallpaper in SystemParametersInfoW function is 20 
    SPI_SETDESKWALLPAPER = 20 

    #Main code to change the wallpaper
    output_from_wallpaper_change = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, getabsolutepath(filename), 0) 
    
    if output_from_wallpaper_change == 1:
        print("Your wallpaper has been changed successfully!!!")
    else:
        print("Sorry cant set this file as your wallpaper")
else:
    sys.exit("Enter a jpg file only please")
