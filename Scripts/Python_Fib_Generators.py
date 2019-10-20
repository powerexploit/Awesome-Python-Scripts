def python_gen(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
        

num = int(input("Up to whichnumber do you want to the fib number: "))
for i in python_gen(num):
    print(i)