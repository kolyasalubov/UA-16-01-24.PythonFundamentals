import re

password = input("Enter the password: ")

while True:
    if len(password) < 6 or len(password) > 16:
        print("Wrong password")
        break
    elif not re.search("[a-z]",password):
        print("Wrong password")
        break
    elif not re.search("[A-Z]",password):
        print("Wrong password")
        break   
    elif not re.search("[$@#]",password):
        print("Wrong password")
        break
    elif not re.search("[0-9]",password):
        print("Wrong password")
        break
    else:
        print("Valid password")
        break