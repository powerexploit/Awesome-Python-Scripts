"""
Which prints the staircase pattern
   #
  ##
 ###
####

"""
def staircase(height):
   """
   This program prints the staircase pattern for the given height (dynamically)
   Params:
       height: height of the staircase as entered by user
   Returns:
       None
   """
   for i in range(1,height+1):
       print(' '*(height-i) + '#'*i)
      
      
if __name__ == '__main__':

   print('Please enter the height of the staircase')      
   height=int(input()) #which accepts the input
   staircase(height)
