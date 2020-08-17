#importing the regexp module in my script
import re

#salutation users
print("Welcome! I am your Calculator")
print("Type 'quit' to terminate\n")

#declaring global variables
previous = 0
run=True

#defining non parametrized function
def performMath():
    global run 
    equn = input("Give me something to calculate:")
    if equn == 'quit':
        print("You exit.")
        print("See you next time.")
        run= False
    else:
        print("You entered:",equn)

#loop with calling the function
while run:
    performMath()

#end of script