#!/usr/local/bin/python3
#logarithms table
import math
def logarithm():
    x = 1.0
    while x < 10.0:
        print(x,'\t',math.log(x))
        x = x + 1.0

logarithm()
