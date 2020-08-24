# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:25:33 2019

@author: Gulshan
"""

'''def areAnagram(string1, string2):
    if sorted(string1)==sorted(string2):
        return 1
    else:
        return 0
    


string1 = 'geeksforgeeks'
string2 = 'forgeeksgeeks'
if (areAnagram(string1, string2)):
    print('strings are anagram')
else:
    print('strings are not anagram')'''
    
from collections import Counter

def checkAnagram(string1, string2):
    return Counter(string1) == Counter(string2)


if __name__ == '__main__':
    string1 = 'geeksforgeeks'
    string2 = 'forgeeksgeeks'
    print(checkAnagram(string1, string2))
 
