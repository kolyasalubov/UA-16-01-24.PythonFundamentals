def count_sheeps(sheep):
    s = 0
    for i in sheep:
        if i is not None: 
            s += i
    return s