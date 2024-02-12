
#XI. Counting sheep
def count_sheeps(list_of_sheeps):
    count = 0
    for sheep in list_of_sheeps:
        if sheep:
            count += 1
    return count
