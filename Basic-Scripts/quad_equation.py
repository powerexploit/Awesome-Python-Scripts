# Python Program to find roots of a Quadratic Equation
# Solve the quadratic equation ax**2 + bx + c = 0


import cmath  # import complex math module

def findRoots( a, b, c):
    """
    If a is 0 then equation is not quadratic but linear,
    So if user enters value of a as zero then its invalid.
    """
    if a == 0:
        print("Invalid")
        return -1
    discriminant = (b * b) - (4 * a * c)
    if(discriminant > 0):
        root_1 = (-b + math.sqrt(discriminant) / (2 * a))
        root_2 = (-b - math.sqrt(discriminant) / (2 * a))
        print("Two Distinct Real Roots Exists: ")
        print("root1 = %.2f and root2 = %.2f" % (root_1, root_2))
    elif(discriminant == 0):
        root_1 = root_2 = -b / (2 * a)
        print("Two Equal and Real Roots Exists: ")
        print("root1 = %.2f and root2 = %.2f" % (root_1, root_2))
    elif(discriminant < 0):
        root_1 = root_2 = -b / (2 * a)
        imaginary = math.sqrt(-discriminant) / (2 * a)
        print("Two Distinct Complex Roots Exists: ")
        print("r1=%.2f+%.2f and r2=%.2f-%.2f" % (root_1, imaginary, root_2, imaginary))

# Main Program       

a = int(input("Please Enter a Value of a Quadratic Equation : "))
b = int(input("Please Enter b Value of a Quadratic Equation : "))
c = int(input("Please Enter c Value of a Quadratic Equation : "))

findRoots(a, b, c)
