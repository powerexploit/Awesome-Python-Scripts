import random
#Sample word list, a file containing words can also be converted into list
world_list = ["ball","account","xerox","laptop","python","Programming","Hangman","mumbai","bangalore"] 
#print(world_list)
word = random.choice(world_list)
blanks = ["_" for i in range(len(word))]
word = word.lower()
Dict = {}
for i in range(len(word)):
    if word[i] not in Dict:
        Dict[word[i]] = [i]
        
    else:
        Dict[word[i]].append(i)
#print(Dict)
print("Let's play Hangman!!\nYou have 7 chances to guess the word")
chances = 7
miss = []
while chances:
    print("Word: "," ".join(blanks))
    ch = input("Guess: ").lower()
    if ch in Dict:
        list1 = Dict[ch]
        for i in list1:
            blanks[i] = ch
        if blanks.count("_") == 0:
            print("Word: "," ".join(blanks))
            print("Yayy!!! You made it!!!!")
            break
    else:
        chances -= 1
        print("Wrong choice! You have ",chances," chances!!! ")
        miss.append(ch)
    print("Misses: ",", ".join(miss))

    #print(ch)
if not chances:
    print("The word is: ",word)
