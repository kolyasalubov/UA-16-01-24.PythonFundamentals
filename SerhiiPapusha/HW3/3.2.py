number = 1234

# WAY 1 -- that will show invalid results if we have more then 4 numbers and break if less then 4
number_to_string = str(number)
num1 = int(number_to_string[0])
num2 = int(number_to_string[1])
num3 = int(number_to_string[2])
num4 = int(number_to_string[3])

sum_of_nums = num1 + num2 + num3 + num4
print(f'Sum of number using way 1 is: {sum_of_nums}')

# WAY 2 - that should work no matter how number changes

sum = 0
for num in number_to_string:
    sum += int(num)

print(f'Sum of number using way 2 is: {sum}')

# reverse order
print(number_to_string[::-1])

# sorted numbers
print(sorted(number_to_string, reverse=False))
