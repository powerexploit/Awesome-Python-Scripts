# https://www.wikiwand.com/en/Happy_number
# http://mathworld.wolfram.com/HappyNumber.html

def square(x):
    return int(x) * int(x)

def happy(number):
    return sum(map(square, list(str(number))))

def is_happy(number):
    seen_numbers = set()
    while number > 1 and (number not in seen_numbers):
        seen_numbers.add(number)
        number = happy(number)
    return number == 1

def is_happy2(n): # recursive
    return (n == 1 or n > 4 and is_happy2(happy(n)))
