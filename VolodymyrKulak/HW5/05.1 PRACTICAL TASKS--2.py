
user_num = int(input("Enter you Fibonacci number "))

prev_num_1, prev_num_2 = 0, 1

if user_num == 1 or user_num == 0:
    print(prev_num_1)
else:
    print(prev_num_1, prev_num_2, end=" ")

for item in range(2, user_num):
    result_num = prev_num_1 + prev_num_2
    prev_num_1 = prev_num_2
    prev_num_2 = result_num
    print(result_num, end=" ")
