import math
num = int(input("Enter a number to check whether it is Armstrong or not : "))

sumEl = 0
temp = num
while temp > 0:
    # To pick out each digits from the number starting from One's place and gradually towards hundred's place
    digit = temp % 10
    # Continue adding the cube of each digit obtained from previous step
    sumEl += digit ** 3
    # Floor function is used to determine the closest integer value
    temp = math.floor(temp / 10)

if num == sumEl:
    print("Its an armstrong number")
else:
    print("Its not an armstrong number")
