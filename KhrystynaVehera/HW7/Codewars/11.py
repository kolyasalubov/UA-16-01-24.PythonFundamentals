# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    name = 0
    for i in sheep:
        if i == True:
            name+=1
    return name