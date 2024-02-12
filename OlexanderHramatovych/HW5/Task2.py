users_number = int(input("Type your number: "))
nz = 0
n1 = 1
b = 0
while b <= users_number:
    print(b, end=(" , "))
    b = n1+ nz
    print(b)
    nz = n1
    n1 = b

