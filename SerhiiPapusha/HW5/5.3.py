user_number = int(input("Enter number\n"))

factorial = 1
if user_number > 0:
    for i in range(1, user_number + 1):
        factorial *= i
    print(factorial)
else:
    print("cannot calculate factorial for negative numbers")