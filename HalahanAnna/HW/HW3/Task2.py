number = int(input("Введіть чотирьохзначне натуральне число: "))

digits = 1
for digits in str(number):
    digits *= int(digits)
reverse = int(str(number)[::-1])
ascending = int(''.join(sorted(str(number))))

print(f"Product number: {digits}")
print(f"Numbers in reverse order: {reverse}")
print(f"Ascending numbers: {ascending}")

print(f"Добуток цифр: {digits}")
print(f"Число у зворотньому порядку: {reverse}")
print(f"Число з відсортованими цифрами (за зростанням): {ascending}")