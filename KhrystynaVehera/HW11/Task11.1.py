def age():
    
    try:
        user_age = int(input("Please enter your age: "))
        if user_age < 0:
            raise ValueError("Error. Your age couldn`t be negative.")
        elif user_age > 0:
            if user_age % 2 == 0:
                print(f"Your age {user_age} is even.")
            else:
                print(f"Your age {user_age} is odd.")
        elif user_age == 0:
            print(f"How you write us. You are only {user_age} years old.")
    except ValueError as e:
        print(e)    

age()

