from itertools import groupby
S=str(input())
print(*[(len(list(c)), int(k)) for k, c in groupby(S)])