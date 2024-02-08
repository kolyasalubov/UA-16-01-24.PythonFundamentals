even_numbers_divided_by_2 = list(range(0,11,2))
odd_unmbers_divided_by_3 = list(range(1,11,2))
not_divisible_by_both = list(range(0,11))

result_list = [] 

for i in even_numbers_divided_by_2:
    if i % 2 == 0:
        result_list.append(i)

print("Even numbers that are divisible by 2:\n",*result_list)

result_list.clear()

for i in odd_unmbers_divided_by_3:
    if i % 3 == 0:
        result_list.append(i)

print("Odd numbers that are divisible by 3:\n",*result_list)

result_list.clear()

for i in not_divisible_by_both:
    if i % 2 != 0 and i % 3 != 0:
        result_list.append(i)

print("Numbers that are not divisible by 2 or 3:\n",*result_list)    
