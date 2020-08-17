import math
print("Area Calculator")
def rectangle(l,b):
	a=l*b
	return a

def square(r):
  a=r*r
  return a

def circle(r):
  a=(22/7)*r*r
  return a

def triangle(x,y,z):
  s=0.5*(x+y+z)
  s1=s*(s-x)*(s-y)*(s-z)
  a=math.sqrt(s1)
  return a

def eq_triangle(r):
  a=(math.sqrt(3)/4)*r*r
  return a

def right_triangle(h,b):
  a=0.5*h*b
  return a

while(True):
  print("\nChoose the shape whose Area you want to calculate:")
  print("\n1) Rectangle")
  print("\n2) Square")
  print("\n3) Circle")
  print("\n4) Scalene Triangle")
  print("\n5) Equilateral Triangle")
  print("\n6) Right-angled Triangle")

  choice=int(input(">"))

  if choice==1:
    print("Enter Length & Breadth")
    x=int(input(">"))
    y=int(input(">"))
    a1=rectangle(x,y)
    print("The area of rectangle is "+str(a1)+" units")
    
  elif choice==2:
    print("Enter Side of Square")
    x=int(input(">"))
    a2=square(x)
    print("The area of square is "+str(a2)+" units")
  
  elif choice==3:
    print("Enter Radius of Circle")
    x=int(input(">"))
    a3=circle(x)
    print("The area of circle is "+str(a3)+" units")

  elif choice==4:
    print("Enter Length of all three Sides of Triangle")
    x=int(input(">"))
    y=int(input(">"))
    z=int(input(">"))
    a4=triangle(x,y,z)
    print("The area of triangle is "+str(a4)+" units")
  
  elif choice==5:
    print("Enter Side of Equilateral Triangle")
    x=int(input(">"))
    a5=eq_triangle(x)
    print("The area of triangle is "+str(a5)+" units")

  elif choice==6:
    print("Enter Height & Base of the triangle")
    x=int(input(">"))
    y=int(input(">"))
    a6=right_triangle(x,y)
    print("The area of rectangle is "+str(a6)+" units")

  else:
    print("You chose to exit the calculator. Program Terminated")
    break
