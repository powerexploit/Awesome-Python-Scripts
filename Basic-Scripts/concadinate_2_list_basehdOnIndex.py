# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:23:56 2020

@author: ninjaac

input : 2 list
output : merged list 

concept : give you the list that is created my concadinate the 2 list bashed on the list index.
"""
#merging the 2 list based on the index

n=["m","na","i","jh"]
m=["y","me","s","on"]

combined_n_m=[]

for i,j in zip(n,m):
    combined_n_m.append(i+j)
    
print(combined_n_m)