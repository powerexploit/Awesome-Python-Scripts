import itertools, random                                                     #import libraries
deck=list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club'])) #Form a deck of cards
random.shuffle(deck)                                                         #Shuffle the cards
#Draw five cards
print("Your combination of cards is: ")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])

                            
