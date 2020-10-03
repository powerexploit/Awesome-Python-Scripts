import random
highest = 10
answer = random.randint(1,highest)
print(answer)
guess = 0
print('please guess a number from 1 and {}:'.format(highest))
while guess != answer:
    guess = int(input())
    if guess == answer:
        print('well done you did it.')
        break
    else:
        if guess < answer:
            print('please guess higher')
        else:
            print('please guess lower')
