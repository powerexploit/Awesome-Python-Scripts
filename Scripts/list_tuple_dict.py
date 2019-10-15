#first program of list
item1=56
item2="main"
listoftwoitems=[item1,item2]
print("output:\n",listoftwoitems)



#second program
a=[5,6,8]
print("length of list : ",len(a))
a.append(6)
print("adding new value in list : ",a)
print("maixmum in list : ",max(a))
print("minimum in list :",min(a))
a.index(6)
print(a)
      


#third program of list related to random module
import random
a=list(range(1,16))
print(a)
random.shuffle(a)
print(a)
random.choice(a)




#program to tuple
#note tuple can not be changed it is immutable
a=(4,5,8,9,'new','items')
b=(10,8,7,2,'last','thing')
print(a)




#fisrt program of dictionaries
a={'name':'aman','age':89,'class':10}
print(a)
print(list(a.keys()))
print(list(a.values()))


#second program of dictionaries
n={}
n["name"]="aman"
n["profession"]="teacher"
print(n)
