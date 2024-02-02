entered_login = input("Enter your login: ").lower()


while "first" in entered_login:
    print("Hello!")
    break
else:
    print("Error")
