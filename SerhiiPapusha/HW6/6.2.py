while True:
    user_input = input("Please enter your login\n")
    # decided to make it not case sensitive
    if user_input.lower() == "first":
        print(f"Hello {user_input}")
        break
    else:
        print("Wrong input")