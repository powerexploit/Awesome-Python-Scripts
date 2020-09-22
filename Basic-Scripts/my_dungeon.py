"""
by Keivaly Pandya
ib: techwithtim
customized, in order to make it super simple for beginners

"""

print("Welcome to MY DUNGEON!!")    
name = input("What is your name? ")     # Learn to use input
age = int(input("What is your age? "))  # we will be using these variables

health = 10

if age >= 16:                           # not an adult game, but still
    print("Yohoooo! You're old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()  # See how "YES", "YeS", "yES" etc are valid even though they all are different strings
    if wants_to_play == "yes":
        print("You are staring with", health, "health.")    # Using variables
        print("Let the QUEST begin!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You win!")

            else:
                print("You fell in the river and lost...")


        else:
            print("You fell down and lost...")

    else:
        print("Ciao...")
else:
    print("You are not old enough to play...")












