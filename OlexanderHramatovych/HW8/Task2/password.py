import re

# user enters the password
password = input("Enter the password: ")

#creating the loop
while True:
    if len(password) < 6 or len(password) > 16: # len of password
        print("Wrong password")
        break
    elif not re.search("[a-z]",password): # there should be at least one lower case
        print("Wrong password")
        break
    elif not re.search("[A-Z]",password): # there should be at least one upper case
        print("Wrong password")
        break   
    elif not re.search("[$@#]",password): # there should be at least special symbol
        print("Wrong password")
        break
    elif not re.search("[0-9]",password): # there should be at least one number
        print("Wrong password")
        break
    else:
        print("Valid password") # if the password is correct
        break