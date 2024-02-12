
intenger_list = [1, 2, 3, 4, 5]

# variant 1

for digit in intenger_list:
    print(float(digit))

# variant 2


float_digit_list = [float(num) for num in intenger_list]

print(' ')
print("Main intenger list:", intenger_list)
print("Changed float list:", float_digit_list)
