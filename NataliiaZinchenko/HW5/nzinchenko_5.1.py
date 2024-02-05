# 5.1 Creating list with integer elements

integer_list = [12, 53, 64, 193, 200, 1000000, 5845475]
float_list = []


x = 0
while x < len(integer_list):
    float_list.append(float(integer_list[x]))
    x+=1


print(integer_list)
print(float_list)
