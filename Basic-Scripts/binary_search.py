def bin_search(n,s):
    low = 0                             # initialize left index
    high = len(n) - 1                   # initialize right index

    while low <= high:
        index = (low + high)//2         # find the mid-point of the list

        if n[index] < s:                # element is in upper half so ignore lower half
            low = index + 1
        elif n[index] > s:              # element is in lower half so ignore upper half
            high = index - 1
        else:
            return index

    return -1                           # if we reach this part of the code, it means the element does not exist

print("Enter the number of numbers you want to search:")
num = int(input())

n = []     # define a new list to hold the numbers to be searched

print("Enter the List of numbers you want to search")
for i in range(num):
    n.append(int(input()))

print("Enter the number you want to search")
s = int(input())
n.sort()                    #binary search only works on sorted lists

ans = bin_search(n,s)

if ans < 0:
    print(s,"was not found in the given list")
else:
    print(s,"found at index", ans)


