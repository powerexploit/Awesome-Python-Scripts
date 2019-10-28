def binarySearch (arr, l, r, x): 
    if (r >= l): 
        mid =int( l + (r - l)/2)
        if (arr[mid] == x): 
            return mid 
        elif (arr[mid] > x): 
            return binarySearch(arr, l, mid-1, x)  
        else: 
            return binarySearch(arr, mid+1, r, x) 
    else: 
        return -1

# Test array 
arr = [23, 43, 47, 104, 402] 
x = 104
result = binarySearch(arr, 0, len(arr)-1, x)   
if (result != -1): 
    print ("Element is present at index %d" % result) 
else: 
    print ("Element is not present in array")
