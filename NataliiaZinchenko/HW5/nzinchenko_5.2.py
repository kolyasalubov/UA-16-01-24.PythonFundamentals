# 5.2 Printing Fibonacci number up to the entered number n

entered_number = int(input("Enter the number at which the output of the Fibonacci number should end: "))

x = 0
y = 1
print(x)
print(y)

while y < entered_number:
    c = x + y
    print(c)
    x = y
    y = c
else:
    print("You've reached the end")
