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
       The staircase pattern
   """
   for index in range(1,height+1):
       print(' '*(height-index) + '#'*index)
      
      
if __name__ == '__main__':
   
   height=int(input('Enter the height of the staircase')) #which accepts the input
   staircase(height)
