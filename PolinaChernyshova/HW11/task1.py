def determine_odd_or_evel(number):
    try:

        if number < 0:
            raise ValueError("Age cannot be less then 0 ")
        elif number % 2 == 0:
            print(f"Your age({number}) is even")
        else:
            print(f"Your age ({number}) is odd")
    except ValueError as e:
        print(e)


try:
    user_number = int(input("Enter your age, for determine is it odd or evel: "))
    determine_odd_or_evel(user_number)
except ValueError:
    print(f"The age cannot be string")
