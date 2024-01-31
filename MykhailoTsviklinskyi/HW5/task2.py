entered_number = int(input("Please enter your nubmer: "))

a, b = 0, 1

print(f"Fibonacci number up to the entered number {entered_number}:", end=' ')

while a <= entered_number:
    print(a, end=' ')
    a, b = b, a + b
print()