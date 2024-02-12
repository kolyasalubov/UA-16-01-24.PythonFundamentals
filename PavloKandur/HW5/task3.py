user_input = int(input("Enter number to calculate the factorial of: "))

factorial_calc = 1

for i in range (1,user_input+1):
    factorial_calc *= i

print(f"Factorial of {user_input} is {factorial_calc}")