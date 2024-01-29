specified_number = input("Enter 4-digits number: ")


# 2.1 Finding product of the digits
if len(specified_number) > 4 or len(specified_number) < 4:
    print("Entered number must be 4 digits only")
else:
    product_of_digits = int(specified_number[0]) * int(specified_number[1]) * int(specified_number[2]) * int(specified_number[3])
    print(f"Product of the specified number digits is: {product_of_digits}")
    print("=====================================")


# 2.2 Writing the number in reverse order
print(specified_number[::-1])
print("=====================================")


# 2.3 Sorting the given number in ascending order
list_from_specified_number = [specified_number[0], specified_number[1], specified_number[2], specified_number[3]]
sorted_list = list_from_specified_number.sort()

for number in sorted(list_from_specified_number):
    print(number)
