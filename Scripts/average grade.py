grades = []
n = 0
v= 0
average = 0

while True:

    mark = input("Insert one Mark: ")


    if mark == "-1":
        grades.sort()
        grades.pop(0)
        for i in grades:
            v = v + int(i)
        average = v / (n-1)

        print("Grades list: " + str(grades))
        print("Average : " + str(average))
        quit()

    else:
        grades.append(mark)
        n = n + 1

#this program make an averange until you insert "-1", eliminating the lowest one.