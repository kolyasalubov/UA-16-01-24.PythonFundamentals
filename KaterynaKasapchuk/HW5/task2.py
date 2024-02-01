quantity = int(input("write quantity of numbers"))
i=0
a=0
b=1
c=0
while i < quantity:
    if i == 0:
        c = 0
    elif i == 1:
        c = 1
    print(c)
    c = a + b
    b = a
    a = c

    i += 1