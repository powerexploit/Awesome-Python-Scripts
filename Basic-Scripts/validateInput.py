#!/usr/bin/python3
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter the number of your age!')

while True:
    print('Select a new password(letter and numbers)')
    password = input()
    if password.isalnum():
        break
    print('Password can on;y have letters & number!')
