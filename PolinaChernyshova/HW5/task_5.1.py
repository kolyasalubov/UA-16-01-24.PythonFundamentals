# Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type. 

import random



my_list = [int(random.random() * 20) for _ in range(10)]
print(my_list)

# first version
for i in range(len(my_list)):
    my_list[i] = float(my_list[i])

# second version, just like trying to write in one line
# my_list = [float(i) for i in my_list]

print(my_list)