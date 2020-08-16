"""[This script is used to detect whether a given word is present in a list of files.
    All the files which contain the specified word gets stored in a seperate folder.

It takes two inputs - 
1.Path of the directory which contains the files.

[Sample path - "C:/Users/<Your System Name>/Desktop/<Target Folder>/"]

2.Word that you want to detect in these files.
[Sample word - "awesome"]

]
"""

import os
import shutil

# Inputs
directory_path = input("Enter the absolute path of the folder: ")
detect_this = input("Enter the word you want to detect in the files: ")

# Condition to omit creation of the folder if it already exists.
if f"Flagged_{detect_this}" not in os.listdir(directory_path):
    os.mkdir(f"Flagged_{detect_this}")

# Creates a list of all the files/directories in the provided path
files = os.listdir(directory_path)

# To omit adding the python script and the folder in the list of files.
files.remove(f"Flagged_{detect_this}")
files.remove("detector.py")

# List to collect the files which contains the target word
flagged_files = []

# Logic to loop over the files and check for the presence of the target word in them and adding them to the flagged_files list.
for file in files:
    with open(file, "r") as f:
        if detect_this.lower() in f.read().lower():
            flagged_files.append(file)


# Looping over the flagged files and moving them to a seperate folder
for file in flagged_files:
    shutil.move(directory_path+file, directory_path +
                "Flagged_"+detect_this)

# To make the output look organised
print(
    f"The script was successfull in detecting {detect_this} in the list of files")
print(" ")
print("Summary of the detection: ")
print(f"Total Files: {len(files)}")
print(f"Files with the target word: {len(flagged_files)}")
print(" ")
print("Thanks for using this script..........")
