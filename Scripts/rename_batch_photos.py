import os

prefix = 'Travel_'
path_folder_photos = '/Users/user/Downloads/photos_folder/'
# Don't forget / in last position of path_folder_photos

files_in_folder = os.listdir(path_folder_photos)

def rename_file(old_name, new_name):
    os.rename(path_folder_photos+old_name, path_folder_photos+new_name)

for index, file in enumerate(files_in_folder, start=1):
    extension = os.path.splitext(path_folder_photos+file)[1]
    new_name = prefix+str(index)+extension
    rename_file(file, new_name)


'''
# Example input folder

IMG_1020.jpg
IMG_1021.jpg
IMG_1023.jpg
IMG_1024.jpg
IMG_1028.jpg

# Example output folder

Travel_1.jpg
Travel_2.jpg
Travel_3.jpg
Travel_4.jpg
Travel_5.jpg
'''
