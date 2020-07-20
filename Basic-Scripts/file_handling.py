#!/usr/bin/python3
#how to handle files using python

#open and write to a file, then read
with open('file.txt', 'w') as f:
    f.write('Hello World, this is a script to learn hoe to read and write files in Python')
    
with open('file.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        print(line)
    