# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)

login = "First"
user_login = input("Enter a login: ")

while login != user_login:
    user_login = input("Sorry, but it`s wrong login. Try again: ")
else:
    print("Our greeting, your login is correct")