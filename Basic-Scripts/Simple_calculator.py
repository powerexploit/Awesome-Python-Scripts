operation = input('''
Please type in the math operation you would like to complete:
1 for addition
2 for subtraction
3 for multiplication
4 for division
''')

num = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

if operation == '1':
    print('{} + {} = '.format(num, num2))
    print(num+num2)

elif operation == '2':
    print('{} - {} = '.format(num, num2))
    print(num-num2)

elif operation == '3':
    print('{} * {} = '.format(num, num2))
    print(num*num2)

elif operation == '4':
    print('{} / {} = '.format(num, num2))
    print(num / num2)

else:
    print('Wrong Input! Please Try Again')
