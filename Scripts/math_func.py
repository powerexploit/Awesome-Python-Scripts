#!/usr/local/bin/python3
#square root
# import math
from math import *                         #with this form of import statement,calls functions in math
a=int(input("enter first number\n"))       #will not need the math prefix dot 
b=int(input("enter second number\n"))

def func():
    if a > b :
        print(sqrt(a))                    #like this
        ## print(math.sqrt(a))
    else:
        print(sqrt(b))
        ## print(math.sqrt(b))
func()

