# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

even_list_num = []
odd_list_num = []
not_divisible_num_2_3 = []

for i in range(1,11):
    if i % 2 == 0:
        even_list_num.append(i)
    elif i % 3 == 0:
        odd_list_num.append(i)
    else:
        not_divisible_num_2_3.append(i)

print(f'Even numbers that are divisible by 2: {even_list_num}')
print(f'Odd numbers, which are divisible by 3: {odd_list_num}')
print(f'Numbers that are not divisible by 2 and 3: {not_divisible_num_2_3}')