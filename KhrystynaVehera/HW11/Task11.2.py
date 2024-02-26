def day_today():

    days = {"1":"Monday",
            "2":"Tuesday",
            "3":"Wednesday",
            "4":"Thursday",
            "5":"Friday",
            "6":"Saturday",
            "7":"Sunday"}
    
    try:
        user_choise = input("Please choose numer from 1-7 to know a day: ")
        if user_choise.isdigit():
            user_choise1 = int(user_choise)
            if 0 < user_choise1 < 8:
                print(f"The {user_choise} day of a week is {days[user_choise]}!" )
            else:
                raise ValueError(f"Error! {user_choise1} is not in range from 1 to 7.")
    except ValueError as e:
        print("Error:", e)
day_today()

