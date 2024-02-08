# Task 2

n = int(input('Enter number: '))

n1 = 0
n2 = 1
next_n = n2
counter = 1

while counter <= n:
    print(next_n)
    counter += 1
    n1, n2 = n2, next_n
    next_n = n1 + n2

