counter = 1

login_dictionary = {}

while counter <= 10:
    login = input("Plese enter your login: ")
    if login == 'First':
        print(f"Greetings, {login}!")
    else:
        print(f"Your login '{login}' is wrong, please try again")
    login_dictionary.update({counter: login})
    counter += 1

print(login_dictionary)
