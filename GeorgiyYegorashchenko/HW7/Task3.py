# Task 3
input_string = str(input('Enter a string to count symbols: '))

def count_symbols(input_string):
    counter = {}
    for sym in set(input_string):
        counter[sym] = input_string.count(sym)
    return counter
    
print(count_symbols(input_string))
