  # -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:22:45 2020

@author: ninjaac

concept: find the rearrange element of list that sum of no two adjacent elemnents is divisible by 3.
"""
"""
input -- space separated numbers

output --- non divisible by 3 combnation and print "yes" if exits or pront "NO"

explanation : if you give [3,6,1,9] the permutation of it first will find, after that check is there any one sum of two adjacent 
                is not divisible by 3.
                [3,6,1,9] combinations are=(3, 6, 1, 9)    (3, 6, 9, 1)    (3, 1, 6, 9)    (3, 1, 9, 6)    (3, 9, 6, 1)    (3, 9, 1, 6)    (6, 3, 1, 9)    (6, 3, 9, 1)    (6, 1, 3, 9)    (6, 1, 9, 3)    (6, 9, 3, 1)    (6, 9, 1, 3)    (1, 3, 6, 9)    (1, 3, 9, 6)    (1, 6, 3, 9)    (1, 6, 9, 3)    (1, 9, 3, 6)    (1, 9, 6, 3)    (9, 3, 6, 1)    (9, 3, 1, 6)    (9, 6, 3, 1)    (9, 6, 1, 3)    (9, 1, 3, 6)    (9, 1, 6, 3) 
                here there are no pair which contain non divisible by 3.
            
            
            if you give [1,2,3,3] 
                the permutations are = (1, 2, 3, 3)    (1, 2, 3, 3)    (1, 3, 2, 3)    (1, 3, 3, 2)    (1, 3, 2, 3)    (1, 3, 3, 2)    (2, 1, 3, 3)    (2, 1, 3, 3)    (2, 3, 1, 3)    (2, 3, 3, 1)    (2, 3, 1, 3)    (2, 3, 3, 1)    (3, 1, 2, 3)    (3, 1, 3, 2)    (3, 2, 1, 3)    (3, 2, 3, 1)    (3, 3, 1, 2)    (3, 3, 2, 1)    (3, 1, 2, 3)    (3, 1, 3, 2)    (3, 2, 1, 3)    (3, 2, 3, 1)    (3, 3, 1, 2)    (3, 3, 2, 1) 
                 we can see that there exsits at least one combinations (3,2,3,1) where sum of two adjacent is not divisible  by 3.


"""

#import itertools for doing the permutation
from itertools import permutations

numbers=input("enter the numbers")
n_string=numbers.split()
n=[]
for i in n_string:
   n.append(int(i)) 

#set the counter for nondivisible pair
global_not_divisible=0

#find the permutation of given number
per=permutations(n)

#iterate through each combinations
for con in per:
    

    #set the counters to Zero
    divisible=not_divisible=0
    
    #iterate through each elemnt in one combination
    for index,value in enumerate(con):

        if index<len(n)-1:
            
            #sum the adjacent elemnts
            sum=con[index]+con[index+1]
            
            
            #chack the divisibility and update the counters
            if sum%3 == 0:
                divisible+=1
            else:
                not_divisible+=1
        
                
        #update the globar non divisible counter
        if not_divisible==len(n)-1:
            print(con)
            global_not_divisible+=1
        
#if any non divisible pair present than print "yes" else "NO"        
if(global_not_divisible>0):
    print("YES")
else:
    print("NO")

