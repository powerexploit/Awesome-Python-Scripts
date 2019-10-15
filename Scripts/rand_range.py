#!/usr/local/bin/python3
# return random number in range
import random
import sys

try:
    rand_min, rand_max = int(sys.argv[1]), int(sys.argv[2])

    random_int = random.randint(rand_min, rand_max)
    print('random number:', random_int)

except ValueError:
    print('only number like value are valid for min, max')

except IndexError:
    print('''
No min or max number was supplied
rand_range.py <min> <max>
    ''')
