from functions_module import *

while True:
    
    user_choice = (input("What action (addition, subtraction, multiplication, division) do you want to perform? ")).lower()

    if user_choice not in ['addition', 'subtraction', 'multiplication', 'division']:
        print(f"Your choice '{user_choice}' is incorrect. Please try again")

    else:
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))

        if user_choice == 'addition':
            print(f"Addition of '{num1}' and '{num2}' is: {addition(num1, num2):.2f}")
            break
        elif user_choice == 'subtraction':
            print(f"Subtraction of '{num1}' and '{num2}' is: {subtraction(num1, num2):.2f}")
            break
        elif user_choice == 'multiplication':
            print(f"Multiplication of '{num1}' and '{num2}' is: {multiplication(num1, num2):.2f}")
            break
        elif user_choice == 'division':
            while int(num2) == 0:
                print("Cannot be divided by 0")
                num2 = float(input("Please enter another second number: "))
            print(f"Division of '{num1}' and '{num2}' is: {division(num1, num2):.2f}")
            break
