
# creating a loop which checks the login
while True:
    login = input("Enter login: ") # login's input
    if login == "First": 
        print("Greetings {}".format(login)) # if login is right, the system greetes the user
    else:
        print(f"Error.\n The data base has not username \"{login}\" ") # else the system types that it is error
    break