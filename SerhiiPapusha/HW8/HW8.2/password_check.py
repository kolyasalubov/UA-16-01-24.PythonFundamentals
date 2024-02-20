# HW 8.2
import re

# variant 1:
# this might be good for password creation when it says where error is
def pass_check():
    while True:
        password = str(input("Please enter your password:\n"))
        special_chars = ["@", "#", "$"]
        has_lower = any(char.islower() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_number = any(char.isdigit() for char in password)
        has_special = any(char in special_chars for char in password)
        length = len(password) >= 6 and len(password) <= 16

        if has_lower and has_upper and has_number and has_special and length:
            print("Password is valid")
            break
        else:
            error_messages = []
            if not has_lower:
                error_messages.append('lower case')
            if not has_upper:
                error_messages.append('upper case')
            if not has_number:
                error_messages.append('number')
            if not has_special:
                error_messages.append('special symbol')
            if not length:
                error_messages.append('less then 6 or more then 16 symbols')
            print("Password is missing following:")
            print("\n".join(error_messages))

pass_check()

# variant 2:
# variant 2 and 3 better for user login, where we do not want to tell them what is wrong exactly
user_pass = str(input("Please enter your password:\n"))
# print(re.findall("[a-z][0-9][A-Z][@#$]", user_pass))

def  pass_check2(password):
    if re.findall('[a-z]', user_pass):
        if re.findall('[A-Z]', user_pass):
            if re.findall('[0-9]', user_pass):
                if re.findall('[@#$]', user_pass):
                    if len(password) >= 6 and len(password) <= 16:
                        return 'Congrats, your login sucessfull'
    return 'Username or password is incorrect'

# print(pass_check2(user_pass))

# variant 3
def pass_check3(password):
    if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$]).{6,16}$', password):
        return 'Congrats, your login sucessfull'
    else:
        return 'Username or password is incorrect'
    
print(pass_check3(user_pass))