#!/usr/bin/python3
mypets = ['Zophie','Poka','fat-tail']
print('enter a per name:')
name = input()
if name not in mypets:
    print('I dont have a pet name ' + name )
else:
    print(name + 'is my pet')
