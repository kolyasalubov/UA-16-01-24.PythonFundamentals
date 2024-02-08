entered_number = int(input("Please enter your nubmer: "))

factorial = 1

for i in range(1, entered_number + 1):
    factorial *= i
else:
    print(f"{entered_number}! =", factorial)
