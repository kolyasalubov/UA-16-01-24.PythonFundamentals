number = input("Please enter four-digit natural number: ")

product_of_digits = [int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])]

reverse_order = number[3] + number[2] + number[1] + number[0]

number_list = [number[0], number[1], number[2], number[3]]
ascending_list = sorted(number_list)

print("The product of the digits of this number: ", product_of_digits)
print("The number in reverse order: ", reverse_order)
print("The number sorted in ascending order: ", *ascending_list,sep='')
