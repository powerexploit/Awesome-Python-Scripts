#!/usr/bin/python3
#dictionary in python

#creating empty dictionary
my_dict = {}

print("Empty Dictionary: ")
print(my_dict)

#Creating a diictionary with int keys and string values then printing it

my_dict = {1: 'Apple', 2: 'Orange', 3: 'Banana'}
print(my_dict)

#You can access the items of a dictionary by referring to its key name, inside square brackets:

orange = my_dict[2]
print(orange)

#Creating a diictionary with string keys and printing it
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(my_dict)

#Another example of accessing items from a dictionary by its keys

model = my_dict["model"]
print(my_dict)

#looping through all the keys in dictionary and printing them

for key in my_dict:
    print('key in dictionary: ',key)

#looping through all the values in dictionary and printing them

for value in my_dict.values():
    print('value in dictionary:',value)

#looping through all the key and values in dictionary and printing them
for key, value in my_dict.items():
  print(key, value)


