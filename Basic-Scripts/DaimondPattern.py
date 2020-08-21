
n=int(input("enter the number of rows")) #Take input

for i in range(n):

    for j in range(1,int((n/2))-i+3):

        print(sep=" ",end=" ")

    for k in range(1,i+2):

        print("*", end=" ")   #print first half of daimond pattern



    print() #line break

for i in range(n):

    for j in range(1,5-(int((n/2))-i+3)+2):

        print(sep=" ",end=" ")

    for k in range(1,5-i):

        print("*", end=" ")

    print()