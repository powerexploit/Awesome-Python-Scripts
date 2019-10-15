#!/usr/bin/python3
#if and elif 

var1=int(input("enter first value:\n"))
var2=int(input("enter second value:\n"))
var3=int(input("enter third value:\n"))

if var1 > var2 & var1 > var3 :
    print(var1,"is greater than",var2,"and",var3)

elif var2 > var1 & var2 > var3 :
    print(var2,"is greater than",var1,"and",var3)

else :
    print(var3,"is greater than",var1,"and",var2)
