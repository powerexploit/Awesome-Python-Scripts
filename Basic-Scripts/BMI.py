weight = float(input("Enter Weight in kgs : "))
height = float(input("Enter Height in cms : "))

bmi = weight * 10000.0 / (height * height)
print("Your BMI is : {:.2f}" .format(round(bmi,2)))