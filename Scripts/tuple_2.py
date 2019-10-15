#!/usr/bin/python
#Tuple is similer to list but only difference it is immutable
item=('john','elliot','warner',1,23,5)
item1=('varun','aldersion',9,8,6)
item2=(5,10,20,80,90,1222)

print("\nElement of first tuple:\n",item)
print("\nElement of second tuple:\n",item1)
print("\nElement of third tuple:\n",item2)

#functions and operations in tuple similer to list

print("\n length of first tuple : ",len(item))
print("\n length of second tuple : ",len(item1))
print("\n length of third tuple : ",len(item2))

print("\n maximum in third tuple : ",max(item2))
print("\n minimum in third tuple : ",min(item2))

#only difference between tuple and list that element of tuple can not be modified
item[0]='arun'
print(item)

item1.append('war')
print(item1)
