# Print Fibonacci numbers up to the entered number n,
# using cycles.

user_num = int(input("Please, input amount of Fibonacci numbers, would you want to see: "))

num_1 = 0
num_2 = 1
num_3 = 0

for i in range(user_num):
    print(num_3)
    num_1 = num_2
    num_2 = num_3
    num_3 = num_1 + num_2