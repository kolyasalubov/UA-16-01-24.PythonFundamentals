# 5.3 Calculating the factorial of entered number

entered_number = int(input("Enter a number to create factorial: "))

for x in range (1, entered_number):
    if x > 2 and x < entered_number:
        factorial = entered_number * (entered_number-1)
        print(f"{entered_number}! = {entered_number} * {entered_number-1}")
        entered_number -= 1
    elif x < 3:
        print(f"{entered_number}! = {entered_number}")

