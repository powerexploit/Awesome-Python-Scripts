import numpy as np
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(9000)


def karatsuba(x,y):
    ''' The function takes two numbers in string format. 
    The Karatsuba algorithm is a fast multiplication algorithm, using Divide and Conquer approach.
    It reduces the multiplication of two n-digit numbers to at most single-digit multiplications in general. '''
    count=0
    m=int(x)
    len1=0
    while(m>0):
        count=count+1
        m=m//10
    len1=count

    n=int(y)
    count1=0
    len2=0
    while(n>0):
        count1=count1+1
        n=n//10
    len2=count1

    if(len1<=1 or len2<=1):
        return (int(x)*int(y))
    else:
        b=int(x)%(10**(len1//2))
        a=(int(x)-b)//(10**(len1//2))
        #x=(10**(len/2))*a+b
        d=int(y)%(10**(len1//2))
        c=(int(y)-d)//(10**(len1//2))
        #y=(10**(len/2))*c+d
        #ans=(a*c)*(10**len)+(b*d)+(a*d+b*c)*(10**(len/2))
        f1=karatsuba(a,c)
        f2=karatsuba(b,d)
        f3=karatsuba(a+b,c+d)
        return (f1*(10**len1)+f2+(f3-f1-f2)*(10**(len1/2)))

var1 = input('Enter number 1')
var2 = input('Enter number 2')
print(karatsuba(var1,var2))

