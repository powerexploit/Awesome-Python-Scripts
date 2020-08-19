def bubbleSort(legend):
    for num in range(len(legend)-1,0,-1):
        for i in range(num):
            if legend[i]>legend[i+1]:
                terayaarhoonmain = legend[i]
                legend[i] = legend[i+1]
                legend[i+1] = terayaarhoonmain

legend = [14,46,43,27,57,41,45,21,70]
bubbleSort(legend)
print(legend)