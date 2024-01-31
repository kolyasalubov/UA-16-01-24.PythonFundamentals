# 5.2 Printing Fibonacci number up to the entered number n

entered_number = int(input("Enter the number at which the output of the Fibonacci number should end: "))

print(0)
print(1)
x = 1
while x < entered_number:
    print(x)
    x+=x
else:
    print("You've reached the end")