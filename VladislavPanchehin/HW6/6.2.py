true_login = 'First'

while True:
    user_login = input("Enter your login: ")
    if true_login == user_login:
        print("Greetings,", user_login)
        break

    elif user_login != true_login:
        print("WRONG! Access denied for user,", user_login)
