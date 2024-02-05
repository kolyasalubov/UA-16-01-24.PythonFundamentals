for n in range(1, 10):

    if n % 2 == 0:
        print(f"{n} - even numbers that are divisible by 2")
    elif n % 2 == 1 and n % 3 == 0:
        print(f"{n} - odd numbers that are divisible by 3")
    else:
        print(f"{n} - numbers that are not divisible by 2 and 3")
