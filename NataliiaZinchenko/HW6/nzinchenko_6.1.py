even_list = []
odd_list = []
exceptions_list = []

for i in range(1,11):
    if i % 2 == 0:
        even_list.append(i)
    elif i % 3 == 0:
        odd_list.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        exceptions_list.append(i)

print(f"Even numbers: {even_list}")
print(f"Odd numbers: {odd_list}")
print(f"Exceptions: {exceptions_list}")