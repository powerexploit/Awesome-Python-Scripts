#Stack is a data Structure in Python. A stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle

class Stack:
     def __init__(self):
         self.items = []

    #isEmpty() 
     def isEmpty(self):
         return self.items == []
    #push()
     def push(self, item):
         self.items.append(item)
    #pop()
     def pop(self):
         return self.items.pop()
