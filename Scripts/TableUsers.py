from tabulate import tabulate

users = [];
while True:
    print('Enter name (or 0 to stop loop):')
    name = input()
    if name == '0':
        break
    print('Enter age')
    
    age = input()
    users.append([name, age])
    
print('')

print(tabulate(users, headers=['Name', 'Age']))
