print("\nWelcome to This Calculator, Developed By Swarup :)\n")
print("Please Choose Your Calculation type, and enter type (ex + - *)")
print("\n    Enter + for Addition \n    Enter - for subtraction \n    Enter / for division \n    Enter * for multiplication \n")
choice = input("Please Enter Your Choice ->> ")
print("\n")
num1 = int(input("Please enter the 1st number - "))
num2 = int(input("Please enter the 2nd number - "))
print("\n")
if choice == "+":
    num4 = num1 + num2
    print("  Your answer is = " + str(num4))
elif choice == "-":
    num4 = num1 - num2
    print("  Your answer is = " + str(num4))
elif choice == "/":
    num4 = num1 / num2
    print("  Your answer is = " + str(num4))
elif choice == "*":
    num4 = num1 * num2
    print("  Your answer is = " + str(num4))
else:
    print("\n Out of range/ Error \n")
    print("Thank you for using our deshi calculator ;) visit again.")