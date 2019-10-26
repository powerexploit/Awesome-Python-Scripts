#! python3
#script for converting file into ZIP file
import os , zipfile
# type folder path where your zip file is kept
os.chdir('Enter text file Path')
#type the file name you want for ZIP file
newZipFile=zipfile.ZipFile('new_zip_file.zip', 'w')
#type file name you want to convert into ZIP file
newZipFile.write('example_text_file_name.txt', compress_type=zipfile.ZIP_DEFLATED)
newZipFile.close()
#it will save new zip file i.e 'new_zip_file.zip' in same folder 
