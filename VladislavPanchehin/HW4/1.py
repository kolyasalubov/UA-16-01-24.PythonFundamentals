# F(n)=F(n−1)+F(n−2)

fib = int(input("Enter your number: "))

f_0 = 0
f_1 = 1

# variant 1
for i in range (2, fib+1):
    print(f_1, end=' ')
    f_0,f_1 = f_1, f_0 + f_1
    

# varian 2

# while 2 <= fib: 
#     f_0,f_1 = f_1, f_0 + f_1
#     print(f_1, end=' ')
#     fib -= 1
  
