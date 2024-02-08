my_list = list(range(15))

for i in range(len(my_list)):
    my_list[i] = float(my_list[i])

print(*my_list)