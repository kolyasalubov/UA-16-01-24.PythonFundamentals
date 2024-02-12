#int_list = [10, 3, 45, 2, 7]
int_list = list(input("Enter list int: "))
float_list = []

for n in int_list:
    float_list.append(float(n))

print(f"Origin list:{int_list}, Modified list (float): {float_list}")
