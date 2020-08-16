# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:42:50 2018

@author: Gulshan
"""


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(sorted(str1))
print(sorted(str2))

if(sorted(str1)==sorted(str2)):
    print("These are Anagrams")
else:
    print("These are not Anagrams")