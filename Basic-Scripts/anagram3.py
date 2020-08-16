# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:25:33 2019

@author: Gulshan
"""

'''def areAnagram(str1, str2):
    if sorted(str1)==sorted(str2):
        return 1
    else:
        return 0
    


str1 = 'geeksforgeeks'
str2 = 'forgeeksgeeks'
if (areAnagram(str1, str2)):
    print('strings are anagram')
else:
    print('strings are not anagram')'''
    
from collections import Counter

def areAnagram(str1, str2):
    return Counter(str1) == Counter(str2)


str1 = 'geeksforgeeks'
str2 = 'forgeeksgeeks'
print(areAnagram(str1, str2))
 