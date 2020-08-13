def selecsort(lst):
    for i in range(len(lst)):
        minpos=i
        for j in range(i,len(lst)):
            if lst[j]<lst[minpos]:
                minpos=j
        (lst[i],lst[minpos])=(lst[minpos],lst[i])

    for item in lst:
        print(item)
selecsort([1,5,87,2,-56,89])
