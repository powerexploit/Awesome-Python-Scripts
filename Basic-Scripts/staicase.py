"""
Which prints the staircase pattern
   #
  ##
 ###
####

"""
n=int(input()) #which accepts the input
for i in range(1,n+1):
    print(' '*(n-i) + '#'*i)
