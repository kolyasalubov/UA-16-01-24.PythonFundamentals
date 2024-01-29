number_1 = int(input("Please enter natural number: "))
number_2 = int(input("Please enter natural number: "))
number_3 = int(input("Please enter natural number: "))
number_4 = int(input("Please enter natural number: "))





product_of_numbers = number_1 * number_2 * number_3 * number_4
reverse = str(number_4) + str(number_3) + str(number_2) + str(number_1)
list = [number_1, number_2, number_3, number_4]
sorted_number = sorted(list)

print(f"{product_of_numbers}  is the product of four-digit natural number.")
print(f"{reverse} is the number in reverse order.")
print(f"{sorted_number} is The sorted number.")