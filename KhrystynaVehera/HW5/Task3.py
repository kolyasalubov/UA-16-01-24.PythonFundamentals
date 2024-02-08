numbers = int(input("Please enter number to calculate factorial: "))

num_1 = 1


for i in range(1, numbers+1):
    num_2= num_1 * i
    num_1=num_2
    
print(f"Factorial of {numbers} is calculated as {num_1}")