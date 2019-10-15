email=input("enter ur email")
password=input("enter ur password")
if '@' in email:
    if email=="abc@gmail.com" and password=="12345":
       print("You are all set")
    elif email=="abc@gmail.com" and password!="12345":
        print("Your password is wrong")
        password=input("enter ur password again")
        if password=="12345":
            print("Try to type correct once")
        else:
            print("Sorry you have failed two times.")
    else:
       print("Wrong email")
else:
    print("Incorrect syntax")
