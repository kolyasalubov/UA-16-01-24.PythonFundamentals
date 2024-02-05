even_numbers = []
odd_numbers_divisible_by_3 = []
numbers_not_divisible_by_2_and_3 = []

for item in range(1, 11):
    if item % 2 == 0:
        even_numbers.append(item)
    elif item % 2 == 1 and (item / 3).is_integer():
        odd_numbers_divisible_by_3.append(item)
    elif not item % 2 == 0 and not (item / 3).is_integer():
        numbers_not_divisible_by_2_and_3.append(item)

print(f"List with numbers are even (divisible by 2): {even_numbers}")
print(f"List with numbers are odd and divisible by 3: {odd_numbers_divisible_by_3}")
print(f"List with numbers aren't divisible by 2 and 3: {numbers_not_divisible_by_2_and_3}")
