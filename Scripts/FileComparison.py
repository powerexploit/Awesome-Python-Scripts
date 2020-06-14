# Script created by Ryan Goudie (https://github.com/RyanGoudie)
# The purpose of this script is to simply compare 2 files and high light the differences.
# This is my first python script sorry if its not as good as it can be.


#Change the "Path to file to suit the dir your file is kept in" 
#This it the file input used by the script to comapre files
File1=open("Path to file")
File2=open("Path to file")


# Reads the first line from the files
file1_line=File1.readline()
file2_line=File2.readline()

line_no = 1


while file1_line != '' or file2_line != '':


    file1_line = file1_line.rstrip()
    file2_line = file2_line.rstrip()
    

    if file1_line != file2_line:
        
       
        if file2_line == '' and file1_line != '':
            print(">+", "Line-%d" % line_no, file1_line)
    
        elif file1_line != '':
            print(">", "Line-%d" % line_no, file1_line)
            
        
        if file1_line == '' and file2_line != '':
            print("<+", "Line-%d" % line_no, file2_line)
     
        elif file2_line != '':
            print("<", "Line-%d" %  line_no, file2_line)

      
        print()

file1_line = File1.readline()
file2_line = File2.readline()

line_no += 1

File1.close()
File2.close()