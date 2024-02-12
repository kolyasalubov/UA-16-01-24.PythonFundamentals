user_input = int(input("enter number\n"))

fibanachi_sequence = [0, 1]
while fibanachi_sequence[-1] < user_input:
        num = fibanachi_sequence[-1] + fibanachi_sequence[-2]
        if num > user_input:
                break
        fibanachi_sequence.append(num)
print(fibanachi_sequence)