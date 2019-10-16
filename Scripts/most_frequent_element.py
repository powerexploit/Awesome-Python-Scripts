# Python3 program to find the most 
# frequent element in an array. 

def mostFrequent(arr, n): 

	# Sort the array 
	arr.sort() 

	# find the max frequency using 
	# linear traversal 
	max_count = 1; res = arr[0]; curr_count = 1
	
	for i in range(1, n): 
		if (arr[i] == arr[i - 1]): 
			curr_count += 1
			
		else : 
			if (curr_count > max_count): 
				max_count = curr_count 
				res = arr[i - 1] 
			
			curr_count = 1
	
	# If last element is most frequent 
	if (curr_count > max_count): 
	
		max_count = curr_count 
		res = arr[n - 1] 
	
	return res 

# Driver Code 
arr = [31, 55, 55, 13, 3, 2, 1] 
n = len(arr) 
print(mostFrequent(arr, n)) 



