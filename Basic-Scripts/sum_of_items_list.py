def sum_of_elements(user_list): #function definition

  '''Function that prints sum of elements in a list
     params: user_list
     returns: None
  ''' 
  answer = 0
  for item in user_list:
    answer += item #stores the sum of elements
  print("Sum of elements in the list:",answer)



if __name__ == "__main__":
  user_list = []   
# number of elemetns as input 
  n = int(input("Enter number of elements:")) 

# iterating till the range 
  print("Enter the elements:")
  for i in range(0, n): 
    elements = int(input())   
    user_list.append(elements) # adding the element

  sum_of_elements(user_list) #function calling


      
