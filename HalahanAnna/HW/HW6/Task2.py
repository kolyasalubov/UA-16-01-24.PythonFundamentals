correct_log= "First"

while True:
    login = input("Enter your login: ")

    if login != correct_log:
        print("Welcome!")
        break 
    else:
        print("Error: the login is already taken, try another one")

