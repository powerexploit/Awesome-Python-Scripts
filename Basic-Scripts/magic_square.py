# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:24:15 2020

@author: Gulshan
"""
'''

What is Magic Square?
=> a square divided into smaller squares each containing a number,
such that the figures in each vertical, horizontal, and diagonal row add up to the same value.

Example:
    2 7 6 
    9 5 1 
    4 3 8 
    The sum of each row/column/diagonal is: 15.0
    
'''

# Function to create Magic Square
def magic_square(n):
    
    magicSquare = []
    for i in range(n):
        listt = []
        for j in range(n):
            listt.append(0)
        magicSquare.append(listt)
            
    i = n//2
    j = n-1
    
    num = n*n
    count = 1
    
    while(count<=num):
        if(i==-1 and j==n):     #condition 4
            j = n-2
            i = 0
        else:
            if(j==n):           # column value is exceeding
                j = 0
                
            if(i<0):           # row  is becoming -1
                i=n-1
                
        if(magicSquare[i][j]!=0):
            j = j-2
            i = i+1
            continue
        
        else:
            magicSquare[i][j] = count
            count+=1
            
        i = i-1
        j = j+1    #condition 1
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
        
    print("The sum of each row/column/diagonal is: "+str(n*(n**2+1)/2))

# Main Function for Magic Square        
if __name__ == '__main__':
    n = int(input("Enter Number To Generate Magic Square"))
    magic_square(n)
            
