def bubble(a,n):
       for i in range(n):
              for j in range(0, n-i-1):
                     if a[j] > a[j+1] :
                            a[j], a[j+1] = a[j+1], a[j]
a =list(map(int, raw_input().split(" ")))
bubble(a,len(a))
for i in range(len(a)):
       print (a[i]), 
