divisible_by_two = [x for x in range(1, 10) if x % 2 == 0]
print(divisible_by_two)
divisible_by_three= [x for x in range(1, 10) if x % 3 == 0]
print(divisible_by_three)
not_divisible = [x for x in range(1, 10) if x % 3 != 0 and x % 2 != 0]
print(not_divisible)