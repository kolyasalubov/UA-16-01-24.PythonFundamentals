n = int(input("print numbers: "))
a,b = 1, 1
while a <= n:
        print(a, end=" ")
        a, b = b, a + b

