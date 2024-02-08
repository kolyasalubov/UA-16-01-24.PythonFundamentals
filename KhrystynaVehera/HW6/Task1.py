list_1 = list(range(10))

even_list = []
odd_list = []
other_list = []

for i in list_1:
    if i%2 == 0:
        even_list.append(i)
    elif i%3 == 0:
        odd_list.append(i)
    elif i%2 != 0 and i%3 != 0:
        other_list.append(i)

print(f"{even_list} are divisible by 2")
print(f"{odd_list} are divisible by 3")
print(f"{other_list} are not divisible by 2 or 3")
