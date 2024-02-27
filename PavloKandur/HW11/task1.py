def age_check(age:int)->str:
    if age < 0:
        raise Exception("Age cannot be negative")
    if age % 2 == 0:
        return 'Your age is even'
    else:
        return 'Your age is odd'
    

try:
    user_input = int(input("Enter your age: "))
    print(age_check(user_input))
except Exception:
    print("Wrong input")
