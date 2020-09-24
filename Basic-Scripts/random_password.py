import random
import string

def get_random_password():
    random_source = string.ascii_letters + string.digits 
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    

    for index in range(6):
        password += random.choice(random_source)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

print(" Random Password is ", get_random_password())

