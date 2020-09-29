#Importing Library
import random

#GENERATE TWO RANDOM STRINGS FROM THE GIVEN LIST
def RandomString(List):
	string1=random.choice(List)		#First random string
	List.remove(string1)			#To avoid repetition of strings removing the first word from the list
	string2=random.choice(List)		#second random string
	
	return string1,string2
	
#GENERATE TWO RANDOM NUMBERS BETWEEN RANGE (0 - 9)
def RandomNumber():
	List=[0,1,2,3,4,5,6,7,8,9]
	number1=random.choice(List)		#First random number
	List.remove(number1)			#To avoid repetition of numbers removing the first word from the list
	number2=random.choice(List)		#Second random number
	
	return number1,number2
	
#GENERATE TWO RANDOM CHARACTERS	
def RandomSpecialChar():
	List=['~','`','!','@','#','$','%','^','&','*','?','+','-','_',';',':','>','<']
	char1=random.choice(List)		#First random character
	List.remove(char1)				#To avoid repetition of characters removing the first word from the list
	char2=random.choice(List)		#Second random character
	
	return char1,char2
	
#GENERATE A RANDOM INDEX FROM PASSWORD STRING	
def RandomIndex(List):
	index=random.choice(List)
	List.remove(index)
	
	return index
	
#Driver program	
if __name__=='__main__':
	
	#Take input from user
	names=list(input('Input the list of easily remembered words').split())
	
	#Creating password using two strings
	string=RandomString(names)
	password=string[0]+string[1]		

	#Uppercasing random characters in password
	IndexList=list(range(0,len(password)))
	index=RandomIndex(IndexList)
	password=password[:index]+password[index].upper()+password[index+1:]
	index=RandomIndex(IndexList)
	password=password[:index]+password[index].upper()+password[index+1:]

	#Adding random numbers in password
	number=RandomNumber()
	index=RandomIndex(IndexList)
	password=password[:index]+str(number[0])+password[index:]
	index=RandomIndex(IndexList)
	password=password[:index]+str(number[1])+password[index:]

	#Adding random special symbols in password
	char=RandomSpecialChar()
	index=RandomIndex(IndexList)
	password=password[:index]+char[0]+password[index:]
	index=RandomIndex(IndexList)
	password=password[:index]+char[1]+password[index:]

	#Printing the generated password
	print('Generated password : ',password)
	
	
