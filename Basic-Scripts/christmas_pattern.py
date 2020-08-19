#Python Program to print a simple christmas tree pattern using asterisk

picture1 = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
] 

def pattern(picture): #function definition
  ''' Pattern() gets an array of values that prints a pattern
      where 0 is going to be ' ', and the 1 is going to be '*'. '''      
  for image in picture:
    for pixel in image:
      if (pixel):
        print('*', end ="")
      else:
        print(' ', end ="")
    print('') 
    
if __name__=="__main__": 
    pattern(picture1) #funcioncalling
    
'''
Sample Output  
   *   
  ***
 *****
*******
   *
   *
'''
  



