
addressbook = {}

print("Welcome to the Address-Book!")
while True:
    # Stampo il menù che viene ristampato ogni volta che un operazione finisce
    s = input(
        "1. Print Address Book"
        "\n2. Search"
        "\n3. Add"
        "\n4. Edit"
        "\n5. Delete"
        "\n6. Exit"
        "\nInsert command: ")

    if s == "1":
        print(addressbook)

    elif s == "2":
        n = input("Who are you looking for?: ")
        if n in addressbook:
            print(addressbook[n])
        else:
            print("Name not found!")


    elif s == "3":
        code = input("Insert Nickname: ")
        code = code.title()

        if code in addressbook:
            print("Contact is already present!!!")
        else:
            name = input("Insert name for " + code + " : ")
            name = name.title()
            number = input("Insert telephone-number for " + code + ": ")
            addressbook[code] = ['Name: ' + name, 'Number: ' + number]



    elif s == "4":

        code = input("Insert Nickname to edit: ")
        code = code.title()
        if code in addressbook:
            print("Contact found!")
            name1 = input("Insert new name: ")
            name1 = name1.title()
            number1 = input("Insert new number: ")
            addressbook[code] = "Name : " + name1, " Number: " + number1
            print(code + " is update!")
        else:
            print("Contact not present!!!")


    elif s == "5":
        name = input("Insert Nickname to delete: ")
        name = name.title()
        if name in addressbook:
            addressbook.pop(name)
            print("Contact " + name + " is delete!")
        else:
            print("Contact not present!!!")

    elif s == "6":
        print("Goodbye!!!")
        quit()


    else:
        print("Insert a valid choice!")
