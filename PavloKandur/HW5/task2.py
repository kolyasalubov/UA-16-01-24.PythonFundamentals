user_input = int(input("Enter the number of fibonacci numbers to be created: "))

fibonacci_list = [0, 1]

for i in range(user_input-2):
    fibonacci_list.append(fibonacci_list[i]+fibonacci_list[i+1])

print(*fibonacci_list)