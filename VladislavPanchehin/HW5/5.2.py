# F(n)=F(n−1)+F(n−2)

fib = int(input("Enter your number: "))

# f_0 = 0
# f_1 = 1

# # variant 1
# for i in range (2, fib+1):
#     print(f_1, end=' ')
#     f_0,f_1 = f_1, f_0 + f_1


# varian 2 Print Fibonacci numbers up to the entered number n

fib_1 = 1
fib_2 = 1


while fib_2 <= fib:
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    print(fib_2, end=' ')
