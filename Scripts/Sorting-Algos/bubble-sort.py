# This script shows a simple implementation of a bubble sort algorithm
# 
# How it works: In order to sort the numbers in inreasing order, the algorithm
# traverses the list. For each element, if its leftmost neighbor is smaller than
# the current element, they swap positions in the list. This traverse process 
# is repeated n-1 times (being n the size of your list), until all elements are in increasing order
# 
# How it performs: This simple implementation will perform in O(n^2) time
# regardless of the initial state of the list.

def bubble_sort(unordered_list): 
    n = len(unordered_list)
    ordered_list = unordered_list
  
    # Traverse through all list elements 
    for i in range(n): 
  
        # Last n-i-1 elements are already in place 
        for j in range(0, n-i-1): 
  
            # if the current element is bigger than the next, swap them
            if ordered_list[j] > ordered_list[j+1]:
                temp =  ordered_list[j]
                ordered_list[j] = ordered_list[j+1]
                ordered_list[j+1] = temp
    
    return ordered_list

unordered_integer_list = [5,3,2,9,0,1,4,8,7,6]

ordered_integer_list = bubble_sort(unordered_integer_list)

print("The final ordered list is:")
print(ordered_integer_list)