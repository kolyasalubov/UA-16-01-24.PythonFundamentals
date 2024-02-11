import string

def password_validation(password):
    
    while True:

        password_contains_lowercase = False
        password_contains_uppercase = False
        password_contains_digit = False
        password_contains_signs = False
        password_contains_less_6_characters = False
        password_contains_more_12_characters = False

        for item in password:
            if item in string.ascii_lowercase:
                password_contains_lowercase = True
                break
        else:
            print("At least 1 letter between [a-z] is required.")
        
        for item in password:
            if item in string.ascii_uppercase:
                password_contains_uppercase = True
                break
        else:
            print("At least 1 letter between [A-Z] is required.")

        for item in password:
            if item in string.digits:
                password_contains_digit = True
                break
        else:
            print("At least 1 number between [0-9] is required.")

        for item in password:
            if item in "$#@":
                password_contains_signs = True
                break
        else:
            print("At least 1 character between [$#@] is required.")

        if len(password) < 6:
            print("Minimum length 6 characters.")
        else:
            password_contains_less_6_characters = True
    
        if len(password) > 16:
            print("Maximum length 16 characters.")
        else:
            password_contains_more_12_characters = True

        if all([password_contains_lowercase,
                password_contains_uppercase,
                password_contains_digit,
                password_contains_signs,
                password_contains_less_6_characters,
                password_contains_more_12_characters]):
            print("Your password is correct.")
            break
        else:
            password = input("Please try again: ")
            

user_password = input("Please enter your password: ")
password_validation(user_password)
