def selecsort(lst):
    ''' It takes a list as input from the user and returns it's sorted version. '''
    for i in range(len(lst)):
        minpos=i
        for j in range(i,len(lst)):
            if lst[j]<lst[minpos]:
                minpos=j
        (lst[i],lst[minpos])=(lst[minpos],lst[i])

    return lst;
        
n = int(input("Enter the number of elements to sort: "))
input_list = []
for element in range(0,n):
    cin = int(input("Enter the element: "))
    input_list.append(cin)

sorted_list = selecsort(input_list)
print(sorted_list)
