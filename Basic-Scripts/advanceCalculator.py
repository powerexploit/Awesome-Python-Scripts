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
    global previous
    equn = ""
    if previous == 0:
        equn = input("Give me something to calculate:")
    else:
        equn = input(str(previous))

    if equn == 'quit':
        print("You exit.")
        print("See you next time.")
        run = False
    else:
        equn = re.sub('[a-zA-z,.:()" "]', '', equn)
        # removing if any words are entered

        if previous == 0:
            previous = eval(equn)
        else:
            previous = eval(str(previous) + equn)

#loop with calling the function
while run:
    performMath()

#end of script