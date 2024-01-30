
# variant 1
num = 2291
num_string = str(num)
convert_num = int(num_string[0]) * int(num_string[1]) * \
    int(num_string[2]) * int(num_string[3])

reverse_num = num_string[::-1]

sorted_num = sorted(num_string)


print('Product number', num, ':', convert_num)
print(f"Reverse number {num}: {reverse_num}")
print(f"Sorted number {num}: {sorted_num}")


# variant 2

# num = int(2291)
# started_counter = 1

# for num_string in str(num):
#     digit = int(num_string)
#     started_counter *= digit
# print(f"Product number '{num}': {started_counter}")
