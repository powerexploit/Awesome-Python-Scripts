filename = input("Enter the file name: ")
text = input("Enter something to write in the file: ")

f = open(filename + ".txt", "w")
f.write(text)
f.close()
