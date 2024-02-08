int_list = [1, 2, 3, 4, 5]

float_list = []

for item in int_list:
    float_list.append(float(item))

print(f"List with integer type: {int_list}, {type(int_list[0])}")
print(f"List with float type: {float_list}, {type(float_list[0])}")