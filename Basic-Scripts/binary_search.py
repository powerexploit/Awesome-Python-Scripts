def binary_search(list1, key):
    start = 0
    end = len(list1)
    while start<end:
        mid = (start+end)//2
        if list1[mid] > key:
            end = mid
        elif list1[mid] == key:
            start = mid+1
        else:
            return mid
        return -1

list1 = input('Enter the sorted list of numbers: ')
list1 = list1.split()
list1 = [int(x) for x in list1]
key = int(input('The number to be searched'))           
index = binary_search(list1 , key)
if index < 0:
    print('{} was not found' .format(key))
else:
    print('{} was found at index {} ' .format(key, index))         