#!/usr/bin/python3
#find length of list and some other stuff

item=['john','elliot','joe',1,5,6]
item1=['wayne','love',10,89,78]
item2=[4,56,8,9,7]

print("\nFirst list:\n",item)
print("\nsecond list:\n",item1)
print("\nthird list:\n",item2)

print("\n",len(item),"is a length of first list")
print("\n",len(item1),"is a length of second list")

print("\n first element of first list is : ",item[0])
print("\n last element of second list is : ",item1[5-1])

print("\nmimimum element in third list : ",min(item2))
print("\nmaximum element in third list : ",max(item2))

print("\nadding a new element in first list 'rock' ")
item.append("rock")
print("\n First list : \n",item)

#
item1[2]='dsf'
print(item1)
