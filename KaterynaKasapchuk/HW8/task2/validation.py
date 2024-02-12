import string 

lower_list = list(string.ascii_lowercase)  
upper_list = list(string.ascii_uppercase)

number_list = [str(i) for i in range(0,10)]
special_list = ["$","@","#"]

contains_lower = False
contains_upper = False
contains_special = False
contains_number = False
accepted_length = False

password = input("Enter your password: ")


while True:
    for character in password:
        if character in lower_list:
            contains_lower = True
            
        if character in upper_list:
            contains_upper = True
            
        if character in number_list:
            contains_number = True
            
        if character in special_list:
            contains_special = True
            
    if len(password) >= 6 and len(password) <= 16:
        accepted_length = True

    if contains_lower and contains_upper and contains_number and contains_special and accepted_length:
        print("The password is valid")
        break
    else:
        print("The password is invalid")
        password = input("Enter your password: ")