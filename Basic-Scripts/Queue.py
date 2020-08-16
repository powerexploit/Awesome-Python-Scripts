from os import sys
class Queue(object):
    def __init__(self):
        self.array=[]
        self.top=0
        self.rear=0

    def isEmpty(self):
        return self.array==[]

    def push(self,item):
        self.array.insert(0,item)
        self.rear+=1

    def pop(self):
        self.array.pop()
        self.rear-=1

    def menu(self):
        char=0
        while char<6:
            print("Press 1 -> To add a element to the Queue")
            print("Press 2 -> To remove a element from the Queue")
            print("Press 3 -> To view the top and rear element of the Queue")
            print("Press 4 -> To view all the elements of the Queue")
            print("Press 5 -> To Exit")
            char=int(input("Enter your choice: "))
            print('\n')
            if char==1:
                val=int(input("Enter the element: "))
                self.push(val)
                print("Your element has been added.")
                print('\n')
            elif char==2:
                if self.isEmpty():
                    print("Queue is underflowed. Please add elements to it.")
                    break
                else:
                    self.pop()
                    print("Your element has been removed")
                    print('\n')
            elif char==3:
                print("Top element ->  {}".format(self.array[self.top]))
                print("Rear element -> {}".format(self.array[self.rear-1]))
                print('\n')
            elif char==4:
                for i in range(0,len(self.array)):
                    if i==len(self.array) - 1:
                        print("{} <- Rear Element".format(self.array[i]))
                    elif i==0:
                        print("{} <- Top Element".format(self.array[0]))
                    else:
                        print(self.array[i])
                    print('\n')
            else:
                sys.exit()

Object1=Queue()
Object1.menu()
                
                
