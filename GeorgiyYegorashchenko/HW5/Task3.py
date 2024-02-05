# Task 3

number = int(input('Enter number to calculate factorial: '))
acc = 1

for i in range(1, number + 1):
    acc = acc * i

print('Factorial = ', acc)
