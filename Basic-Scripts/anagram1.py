# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:31:58 2018

@author: Gulshan
"""


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

count1 = 0
i = 0
while(i<len(str1)):
    count1 = count1+ord(str1[i])
    i = i+1
print("1st",count1)

count2 = 0
j = 0
while(j<len(str2)):
    count2 = count2+ord(str2[j])
    j = j+1
print("2nd",count2)

if(count1==count2):
    print("These are Anagrams")
else:
    print("These are not Anagrams")
    