# Python Program to find roots of a Quadratic Equation
# Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module
import cmath
a = int(input("Please Enter a Value of a Quadratic Equation : "))
b = int(input("Please Enter b Value of a Quadratic Equation : "))
c = int(input("Please Enter c Value of a Quadratic Equation : "))

discriminant = (b * b) - (4 * a * c)

if(discriminant > 0):
    r1 = (-b + math.sqrt(discriminant) / (2 * a))
    r2 = (-b - math.sqrt(discriminant) / (2 * a))
    print("Two Distinct Real Roots Exists: ")
    print("root1 = %.2f and root2 = %.2f" % (r1, r2))
elif(discriminant == 0):
    r1 = r2 = -b / (2 * a)
    print("Two Equal and Real Roots Exists: ")
    print("root1 = %.2f and root2 = %.2f" % (r1, r2))
elif(discriminant < 0):
    r1 = r2 = -b / (2 * a)
    imaginary = math.sqrt(-discriminant) / (2 * a)
    print("Two Distinct Complex Roots Exists: ")
    print("r1=%.2f+%.2f and r2=%.2f-%.2f" % (r1, imaginary, r2, imaginary))

