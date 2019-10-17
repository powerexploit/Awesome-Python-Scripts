#!/usr/bin/python3
#This program will receive an input from the user and count how many time each digit appears
letter_counter={}

for letter in input("I want to count the letters of: ").lower():
    if letter in letter_counter:
        letter_counter[letter] += 1
    else:
        letter_counter[letter] = 1

for letter in letter_counter:
    print("#" + letter + ":", letter_counter[letter])