# Task 1
list1 = []
for i in range(1, 10):
    if i%2 == 0:
        list1.append(i)
        print(list1)


list2 = []
for n in range(1, 10):
    if n%3 == 0 and n%2 != 0:
        list2.append(n)
        print(list2)


list3 = []
for m in range(1, 10):
    if m%3 !=0 and m%2 !=0:
        list3.append(m)
        print(list3)