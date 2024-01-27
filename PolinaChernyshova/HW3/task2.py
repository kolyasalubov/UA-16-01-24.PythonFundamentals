# A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number

users_number = input('Input your four-digit natural number ')

while not users_number.isdigit() or len(users_number) != 4:
    users_number = input('Sorry, you input wrong number. Please, input your new number ')

sum_of_numbers = int(users_number[:1]) * int(users_number[1:2]) * int(users_number[2:3]) * int(users_number[3:4])
reverse_number = users_number[::-1]
sorted_number = ''.join(sorted(users_number))

print(f'Your number = {users_number}')
print(f'Sum of number = {sum_of_numbers}')
print(f'Reversed number = {reverse_number}')
print(f'Sorted number = {sorted_number}')

#I solved it this way, before realizing that we had worked without a loop

# sum_of_numbers = 0 
# reverse_number = ''
# list_num = []
# for i in range(4):
#     sum_of_numbers += tmp1 % 10
#     reverse_number += str(tmp1 % 10)
#     list_num.append(tmp1 % 10)
#     tmp1 //= 10

# list_num.sort()
# sorted_number = ''
# for i in list_num:
#     sorted_number += str(i)

# reverse_number = int(reverse_number)
# sorted_number_int = int(sorted_number) #if needed to work with int,but without 0 in number
