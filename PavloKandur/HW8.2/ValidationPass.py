import string
def validation(password:str)-> bool: 
    answear = True
    current_answear = 6<len(password)<16
    answear = answear and current_answear
    for i in password:
        if i in string.ascii_lowercase:
            current_answear = True
            break
        else:
            current_answear = False
    answear = answear and current_answear
    for i in password:
        if i in string.ascii_uppercase:
            current_answear = True
            break
        else:
            current_answear = False
    answear = answear and current_answear
    for i in password:
        if i in '0123456789':
            current_answear = True
            break
        else:
            current_answear = False
    answear = answear and current_answear
    for i in password:
        if i in '#$@':
            current_answear = True
            break
        else:
            current_answear = False
    answear = answear and current_answear
    return answear



user_input=(input("Enter password for validation: "))
if validation(user_input):
    print("Password is good")
else:
    print("Password is bad")
