#!/usr/bin/python3
#a program that takes a range of numbers and prints fizz if number is even or buzz if the number is odd
#can also add functionality for user to enter their own range


def fizz_buzz():
    for i in range(5, 13):
        if i%2==0:
            print("Fizz")
        elif i%2==1:
            print("Buzz")
        else:
            print("Invalid input")


fizz_buzz()