
import random
print("Number guessing game")
number = random.randint(1, 99)
chances = 0
print("Guess a number (between 1 and 99):")
while chances < 8:
    guess = int(input())
    if guess == number:
        print("Hooray YOU WON!!!")
        break
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)
    else:
        print("Your guess was too high: Guess a number lower than", guess)
    chances += 1
if not chances < 8:
    print("YOU LOSE!!! The number is", number)
