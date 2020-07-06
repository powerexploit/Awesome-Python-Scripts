#first define the functions
#for 2 digits oprations
def add(x, y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def power(x,y):
    return pow(x, y)

#take input from user
print("Select opration:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.power")
select=input("Enter any one Choice from 1 to 5 :")

num1=int(input("Enter the Num1:"))
num2=int(input("Enter the Num2:"))

if select=="1":
    print(num1,"+",num2,"=", add(num1,num2))
elif select=="2":
    print(num1,"-",num2,"=", sub(num1,num2))
elif select=="3":
    print(num1,"x",num2,"=", mul(num1,num2))
elif select=="4":
    print(num1,"/",num2,"=", div(num1,num2))
elif select=="2":
    print(num1,"*",num2,"=", power(num1,num2))
else :
    print("Not a valid input! tru again")