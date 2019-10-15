#!/usr/bin/python
#Factorial program using while loop

n=int(input("\nEnter the number:\n"))
f=1

i=1
while(i<=n):
    f=f*i
    i=i+1

print("\n factorial of number",n,"is:",f)
