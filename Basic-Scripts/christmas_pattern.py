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
  ''' 
    Functions prints the pattern of christmas tree
      where 0 is going to be ' ', and the 1 is going to be '*'.
      params:
      picture: Contains the binary representation of christmas tree
    returns:
      None
      
  '''      
  for image in picture:
    for pixel in image:
      if (pixel):
        print('*', end ="")
      else:
        print(' ', end ="")
    print('') 
    
if __name__=="__main__": 
    pattern(picture1) #funcion calling
    
'''
Sample Output  
   *   
  ***
 *****
*******
   *
   *
'''
  



