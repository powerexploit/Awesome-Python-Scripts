import numpy as np
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(9000)
#x=3141592653589793238462643383279502884197169399375105820974944592
#y=2718281828459045235360287471352662497757247093699959574966967627
#len=64
#x=5678
#y=1234
#l=4
#b=x%100
#a=(x-b)/100
#d=y%100
#c=(y-d)/100
#ans=(a*c)*(10**4)+(b*d)+(a*d+b*c)*100
#print(ans)


#b=x%(10**(len/2))
#print(b)
#a=(x-b)/(len/2)
#x=(10**(len/2))*a+b
#d=y%(10**(len/2))
#print(d)
#c=(y-d)/(len/2)
#y=(10**(len/2))*c+d
#ans=(a*c)*(10**len)+(b*d)+(a*d+b*c)*(10**(len/2))
#print(ans)
#for equal digits in x and y
def karatsuba(x,y):
    #len1=len(x)
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

var1=str(3141592653589793238462643383279502884197169399375105820974944592)
var2=str(2718281828459045235360287471352662497757247093699959574966967627)
print(karatsuba(var1,var2))
#print(karatsuba(1200,1400))
