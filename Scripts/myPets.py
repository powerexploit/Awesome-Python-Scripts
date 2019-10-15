#!/usr/bin/python3

mypets = ['Zophie','Poka','fat-tail']

name = input('Enter pet name: ')

if name not in mypets:
    print('I dont have a pet name "%s"' % name )
else:
    print(name + ', is my pet')
