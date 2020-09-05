# Script of Advance Calculator using Python using regexp module

# importing the regexp module
import re

# salutation and providing termination condition.
print("Welcome! I am your Advance Calculator.")
print("Type 'quit' to terminate.\n")

#declaring global variables
previous_value = 0
flag = True

# Defining non parametrized function to perform all the operations. 
def calculate():
    global flag 
    global previous_value 

    equation = ""
    
    # Taking input from the user.
    if previous_value == 0:
        equation = input("Give me something to calculate:")
    else:
        equation = input(str(previous_value))

    # Termination step.
    if equation == 'quit':
        print("You exit.")
        print("See you next time.")
        flag = False
    else:
        equation = re.sub('[a-zA-z,.:()" "]', '', equation)
        # For security point of view here we eliminate all the letters and keep only numerical characters, if entered by the user.

        # Calculating the results.
        if previous_value == 0:
            previous_value = eval(equation)
        else:
            previous_value = eval(str(previous_value) + equation)

# Calling the function within the infinite loop.
# On execution will continue to calculate until the user enters 'quit' .
while flag:
    calculate()

#end of the script