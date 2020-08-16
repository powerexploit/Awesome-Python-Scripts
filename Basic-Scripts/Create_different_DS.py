inp = int(input('Enter the Range of numbers :'))
lst = []
for num in range(inp):
    lst.append(num)
    tup = tuple(lst)
    st = set(lst)
print("List :", lst)
print("Tuple :", tup)
print("Set :", st)
