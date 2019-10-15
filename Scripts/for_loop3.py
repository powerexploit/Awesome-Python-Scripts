#!/usr/bin/python
#Finding factorial of number using for loop

n=int(input("\nenter the number:\n"))
f=1
for i in range(1,n):
    i=i+1
    f=f*i

print("\nfactorial of number ",n,"is : ",f)
