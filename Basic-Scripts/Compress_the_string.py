from itertools import groupby
S=str(input())                                          # user input for string
print(*[(len(list(c)), str(k)) for k, c in groupby(S)]) # logic to print occurence of values in string 
