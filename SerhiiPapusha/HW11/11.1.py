def age_odd_even():
    while True:
        try:
            age = int(input("Enter your age\n"))
            if age <= 0:
                raise ValueError("Age cannot be less or equal 0! Try again")
            elif age % 2 == 0:
                return "Age is even"
            else:
                return "Age is odd"
        except ValueError as e:
            print(e)
print(age_odd_even())