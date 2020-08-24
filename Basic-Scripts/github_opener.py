import os
import sys
import pyperclip

# Install pyperclip module. Linux OS : sudo apt install python3-pyperclip
#                           otherwise : pip3 install pyperclip

def github_opener (filename, line_no):
    """
    github_opener( filename, line_no ) : 
    Generates a perma link to the code inside your Github repo which is remote for your current git project. 
    And copies it to clipboard. 

    Parameters:
    github_opener ( filename, line_no ) : takes two arguments. 
    Filename in which the code is and line no which you want to highlight.
    eg. github_opener("hello.py", 8)

    Returns:
    Perma link copied to clipboard

    """
    
    stream = os.popen('git remote -v | grep "origin"')
    cmd_output = stream.readline()                          #cmd_output => origin  git@github:username/proj/name.git (fetch)
    info = cmd_output.split(":")[1].split(".")[0]           #info => username/proj_name
    
    curr_dir = os.getcwd()
    
    proj_name = info.split("/")[1]                          #proj_name
    index = curr_dir.find(proj_name)                        #start index of proj name in current path
    perma_link = "https://github.com/" + info + "/blob/master" + curr_dir[(index+len(proj_name)):] + "/" + filename + "/#L" + line_no
    pyperclip.copy(perma_link)
    print("Link copied!")
    
if __name__ == "__main__":
    """
    It takes two command line arguments.
    Name of the file (Not complete path with directory) in which the desired line of code is present and 
    the line number to high light.
    Eg. 
        python github_opener.py mode.py 9
    output:
        Link copied!
        (Link => https://github.com/username/proj_name/blob/master/directory/mode.py/#L9)


    In terminal, navigate to the directory in which the file is present.

    Run command : python github_opener.py filename.xyz 23

    """
    github_opener(sys.argv[1], sys.argv[2])