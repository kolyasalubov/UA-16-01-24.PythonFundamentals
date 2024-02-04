while True:
    user_login = input("Enter you login: ")
    
    if user_login == "First":
        print(f"Greetings {user_login}!")
        break
    else:
        print(f"Eror, this user name {user_login} is not in database. Please try again or sign up.")
