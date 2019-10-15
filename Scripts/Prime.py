#!/usr/bin/python
#Program to find prime and non prime number 
no=int(input("Enter the number:\n"))
b=0
for i in {1,50}:

    if no%i == 0:
        b=b+1

if b == 2:
    print(no,"is prime number:\n")
else:
    print(no,"is non prime number:\n")
