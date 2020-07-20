# Python3 program to find simple interest 
# for given principal amount, time and 
# rate of interest. 

# We can change values here for 
# different inputs 
P = int(input("Enter the Principal value"))
R = float(input("Enter the rate"))
T = int(input("Enter the time duration"))

# Calculates simple interest 
SI = (P * R * T) / 100

# Print the resultant value of SI 
print("Simple interest is", SI) 


