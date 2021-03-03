#paste the location of your folder in path variable
# if location is:  C:\Users\raees\Downloads\Test
# Then the path variable should be: path = r'C:\Users\raees\Downloads\Test'


import os
import time
from os import listdir
from os.path import isfile, join


files = []
folders = []

def scan():
    for f in listdir(path):
        if(f not in files and f not in folders):
            if(isfile(join(path, f))):
                files.append(f)
            else:
                folders.append(f)

def mkdir(name):
    if(name not in folders):
        os.mkdir(path + '\\' + name)

def check(ext,file):
    if(ext in file):
        return True
    else:
        return False

def checkMulti(ext,file):
    for e in ext:
        if(e in file):
            return True
    return False

def organize(items):

    for file in items:
            curPath = path +'\\' + file
            if(check('.py',file)):
                scan()
                mkdir('Python')
                desPath = path +'\\Python\\' + file
                print('Adding ' + file + ' to ' + ' Python')
                os.rename(curPath,desPath)
                
            elif(check('.cpp',file)):
                scan()
                mkdir('C++')
                desPath = path +'\\C++\\' + file
                print('Adding ' + file + ' to ' + ' C++')
                os.rename(curPath,desPath)

            elif(checkMulti(['.png','.jpeg','.jpg'],file)):
                scan()
                mkdir('Images')
                desPath = path +'\\Images\\' + file
                print('Adding ' + file + ' to ' + ' Images')
                os.rename(curPath,desPath)

            elif(checkMulti(['.mp4','.mkv','.avi','.m4v'],file)):
                scan()
                mkdir('Videos')
                desPath = path + '\\Videos\\' + file
                print('Adding ' + file + ' to ' + ' Videos')
                os.rename(curPath,desPath)

            elif(checkMulti(['.mp3','.wav','.aac','.wma'],file)):
                scan()
                mkdir('Audio')
                desPath = path + '\\Audio\\' + file
                print('Adding ' + file + ' to ' + ' Audio')
                os.rename(curPath,desPath)

            elif(checkMulti(['.doc','.docx'],file)):
                scan()
                mkdir('Documents')
                desPath = path +'\\Documents\\' + file
                print('Adding ' + file + ' to ' + ' Documents')
                os.rename(curPath,desPath)

            elif(check('.pdf',file)):
                scan()
                mkdir('Pdfs')
                desPath = path +'\\Pdfs\\' + file
                print('Adding ' + file + ' to ' + ' Pdfs')
                os.rename(curPath,desPath)

            else:
                scan()
                mkdir('Other')
                desPath = path +'\\Other\\' + file
                print('Adding ' + file + ' to ' + ' Other')
                os.rename(curPath,desPath)

path = r'C:\Users\raees\Downloads\Test'
scan()

while(True):
    time.sleep(10)
    after = [f for f in os.listdir(path) if isfile(join(path,f))]
    added = [f for f in after if not f in files]
    if len(added)!=0 or len(files) !=0:
        try:
            organize(added)
            organize(files)
        except:
            pass
