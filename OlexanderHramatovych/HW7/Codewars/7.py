def solution(number):
    l = []
    for n in range(1,number):
        if n % 3 == 0 or n % 5 == 0:
            l.append(n)
    return sum(l)
print(solution(6))