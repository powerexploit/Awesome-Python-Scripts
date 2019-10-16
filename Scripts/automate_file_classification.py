
#the rules.txt file contains the necessary info and rules for moving the files 

import os
import shutil

#the following lines indicate the path of the rules.txt file

file_path = os.getcwd()
file_name = os.path.join(file_path, "rules.txt")
    

#get the path and the mode from rules.txt

file_t = open(file_name,'r')
path = file_t.readline()
mode = file_t.readline()
mode = mode.strip("\n")
path1 = path.strip("\n")

#the following function returns a dictionary that contains the rules. The dictionary's keys behave as extensions of the files and values act as moved paths

dict1 = {}   
def rules():
    dict1 = {}
    for each in file_t:
        each = each.strip("\n")
        if each.split(":",1)[0]:
            file_ext,dest_path = each.split(":",1)
            file_ext = file_ext.strip()
            dest_path = dest_path.strip()
            dict1[file_ext] = dest_path
    return dict1


#the following function takes a list of files and moves the files to their resp files

def file_move(files_list):
    for file in files_list:
        if "." in file:
            ext = file.rsplit(".",1)[1]
            ext = ext.strip()
            if ext in dict1:
                dst = dict1[ext]
                try:
                    print (file)
                    shutil.move(file,dst)
                except Exception as e:
                    print (e)    

#the following function is used when a simple mode is selected

def single_dir(path1):
    os.chdir(path1)
    files = os.listdir(".")
    file_move(files)

#the following function is used when recursive mode is selected    

def rec_dirs(path1):
    for root,dirs,files in os.walk(path1,topdown=True,onerror=None,followlinks=False):
        #print files
        os.chdir(root)
        file_move(files)
        print("files are moved")

dict1 = rules()

rec_dirs(path1)


       