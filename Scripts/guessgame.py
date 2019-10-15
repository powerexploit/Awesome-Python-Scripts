#this is a guessing the no. game
import random
secretno=random.randint(1,20)
print("i guessed a no. between 1 to 20","u need to guess what i guessed")
#ask the user to guess the no. giving a chance of 6 times
for guessesTaken in range(1,6):
    print("guess any no.")
    guess=int(input())
    if guess<secretno:
        print("ur guess is low")
    elif guess>secretno:
        print("ur guess is high")
    else:
        print("congo")
        break
if guess==secretno:
    print("u guessed the no. in "+str(guessesTaken)+" no of times")
else:
    print("sorry u failed...i was thinking of "+str(secretno))
    
