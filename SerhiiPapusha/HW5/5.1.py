# Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.

list = list(range(0, 20, 3))
# print(type(list[2]))

# WAY WITH FOR LOOP
for num1 in list:
    num1 = float(num1)
    print(f"{num1} type is {type(num1)}")
# WAY WITH WHILE LOOP
i = 0
while i < len(list):
    num = float(list[i])
    print(f"{num} type is {type(num)}")
    i += 1