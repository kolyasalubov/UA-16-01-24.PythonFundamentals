users_number = int(input("Type integer number to calculate the factorial(!): "))
multiply = 1


if users_number == 0:
    print(f"{users_number} = 1")
elif users_number < 0:
    print("Factorial is only for numbers that are > 0")
else: 
    for n in range (1,users_number+1):
        multiply = n * multiply
print(f"{users_number}! = {multiply}")

