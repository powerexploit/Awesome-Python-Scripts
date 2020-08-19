# Python program to count positive and negative numbers in a List 
  
# list of numbers 
list1 = [10, -21, 4, -45, 66, -93, 1] 

positive_count, negative_count = 0, 0
  
# iterating each number in list 
for num in list1:     
    # checking condition 
    if num >= 0: 
        positive_count += 1
    else: 
        negative_count += 1
          
print("Positive numbers in the list: ", positive_count) 
print("Negative numbers in the list: ", negative_count) 
