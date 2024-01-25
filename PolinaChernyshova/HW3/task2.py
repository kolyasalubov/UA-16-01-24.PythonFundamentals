# A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number

users_number = int(input('Input your four-digit natural number '))

while users_number < 999 or users_number > 9999:
    users_number = int(input('Sorry, you input wrong number. Please, input your new number '))
tmp1 = users_number

sum_of_numbers = 0 
reverse_number = ''
list_num = []
for i in range(4):
    sum_of_numbers += tmp1 % 10
    reverse_number += str(tmp1 % 10)
    list_num.append(tmp1 % 10)
    tmp1 //= 10

list_num.sort()
sorted_number = ''
for i in list_num:
    sorted_number += str(i)

reverse_number = int(reverse_number)
sorted_number_int = int(sorted_number) #if needed to work with int,but without 0 in number

print(f'Your number = {users_number}')
print(f'Sum of number = {sum_of_numbers}')
print(f'Reversed number = {reverse_number}')
print(f'Sorted number = {sorted_number}')
