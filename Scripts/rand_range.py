#!/usr/local/bin/python3
# return random number in range
import random
import sys

print('----------------------------------------')
try:
    rand_min, rand_max, n = int(sys.argv[1]), int(sys.argv[2]), ( int(sys.argv[3]) if len(sys.argv) > 3 else 1 )

    random_ints = []
    
    if n == 1:
        print('random number:', random.randint(rand_min, rand_max))
    else:
        for i in range(n):
            random_int = random.randint(rand_min, rand_max)
            print('\trandom number:', random_int)
            random_ints.append(random_int)

        print('----------------------------------------')
        print(f'min: {min(random_ints)}, max: {max(random_ints)}, avg: {sum(random_ints)/len(random_ints)}')

except ValueError:
    print('only number like value are valid for min, max')

except IndexError:
    print('''
No min or max number was supplied
rand_range.py <min> <max>
    ''')
