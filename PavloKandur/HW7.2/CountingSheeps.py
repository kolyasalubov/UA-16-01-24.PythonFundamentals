def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i:
            counter +=1
        else:
            continue
    return counter