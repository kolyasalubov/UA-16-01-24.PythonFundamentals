correct_login = 'First'

while True:
    user_login = input("Enter your login: ")
    
    if user_login == correct_login:
        print("Congrats,", user_login)
        break
    else:
        print("Error! Login is incorrect,", user_login)
        