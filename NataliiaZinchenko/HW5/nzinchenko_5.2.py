# 5.2 Printing Fibonacci number up to the entered number n

entered_number = int(input("Enter the number at which the output of the Fibonacci number should end: "))

previous = 0
current = 1
print(previous)
print(current)

while y < entered_number:
    next = previous + current
    print(next)
    previous = current
    current = next
else:
    print("You've reached the end")
