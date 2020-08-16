from os import sys
class Stack(object):
    def __init__(self):
        self.array=[]
        self.reverse=[]
        self.top=0

    def push(self,item):
        self.array.append(item)
        self.top+=1
        

    def pop(self):
        self.top-=1
        self.array.pop()
    

    def isEmpty(self):
        return self.array==[]

    def menu(self):
        char=0
        while char<6:
            print("Press 1 -> To add a element in the Stack")
            print("Press 2 -> To remove a element from the Stack")
            print("Press 3 -> To veiw the top element of the Stack")
            print("Press 4 -> To display all the elements of the Stack")
            print("Press 5 -> To Exit")
            print('\n')
            char=int(input("Enter your choice: "))
            print('\n')
            if char==1:
                val=int(input("Enter the value you want to add: "))
                self.push(val)
                print("Your item {} has been added.".format(val))
                print('\n')
            elif char==2:
                if self.isEmpty():
                    print("Stack underflowed! Please add items into the stack")
                    print('\n')
                    break
                else:
                    self.pop()
            elif char==3:
                print("The top item is -> {}".format(self.array[self.top-1]))
                print('\n')
            elif char==4:
                print("The Stack: ")
                self.reverse=self.array[::-1]
                for i in range (0,len(self.reverse)):
                    if i == 0:
                        print("{} <- Top Item".format(self.reverse[i]))
                    else:
                        print(self.reverse[i])
            else:
                sys.exit()
                        
Object1=Stack()
Object1.menu()
