even = []
odd = []
other = []
for i in range(1,11):
    if i % 2 == 0:
        even.append(i)
    elif i % 3 == 0 and i % 2 == 1:
        odd.append(i)
    else:
        other.append(i)
print("Even numbers: ")
for i in even:
    print(i)
print("Odd numbers divisible by 3: ")
for i in odd:
    print(i)
print("Other numbers: ")
for i in other:
    print(i)