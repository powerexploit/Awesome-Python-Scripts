# this is a python program to find the sum of all numbers in the list except the current index



from functools import reduce

input_array = input("Please enter the array....\n")
print("Multiplication started.....\n")

original_array = list(map(int, input_array.split(' ')))

lst_to_multiply = []
new_lst = []

for i in range(0,len(original_array)):
    if i != 0 and i != len(original_array):
        lst_to_multiply = original_array[0:i] + original_array[i+1:]
    if i == 0:
        lst_to_multiply = original_array[i+1:]
    if i == len(original_array):
        lst_to_multiply = original_array[0:len(original_array)-1]
    # print("lst_to_multiply>>>>", lst_to_multiply)
    new_lst.insert(i, reduce((lambda x,y: x * y), lst_to_multiply))

print("NEW_LST", new_lst)
