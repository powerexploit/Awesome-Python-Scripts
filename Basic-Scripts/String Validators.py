#This is the program to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
S = input()
print(any(char.isalnum() for char in S))
print(any(char.isalpha() for char in S))
print(any(char.isdigit() for char in S))
print(any(char.islower() for char in S))
print(any(char.isupper() for char in S))

#Check the string  by using the methods: .isalnum(), .isalpha(), .isdigit(), .islower() and .isupper().

#str.isalnum() : This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
#str.isalpha() : This method checks if all the characters of a string are alphabetical (a-z and A-Z).
#str.isdigit() : This method checks if all the characters of a string are digits (0-9).
#str.islower() : This method checks if all the characters of a string are lowercase characters (a-z).
#str.isupper() : This method checks if all the characters of a string are uppercase characters (A-Z)
