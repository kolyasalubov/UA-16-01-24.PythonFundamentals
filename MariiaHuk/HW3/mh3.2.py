number = input('Enter a four digit number: ')

digit1 = int(number[0])
digit2 = int(number[1])
digit3 = int(number[2])
digit4 = int(number[3])

digits_list=[digit1, digit2, digit3, digit4]
product_of_digits = digit1 * digit2 * digit3 * digit4
reversed_order = number[::-1]
ascending_order = sorted(number)

print(f"Product of digits: {product_of_digits}")
print(f"Numbers in reverse order: {reversed_order}")
print(f"Numbers in ascending order: {ascending_order}")

