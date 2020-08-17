"""
Which prints the staircase pattern
   #
  ##
 ###
####

"""
def staircase(height):
   for i in range(1,height+1):
       print(' '*(height-i) + '#'*i)
      
      
if __name__ == '__main__':

   print('Please enter the height of the staircase')      
   height=int(input()) #which accepts the input
   staircase(height)
