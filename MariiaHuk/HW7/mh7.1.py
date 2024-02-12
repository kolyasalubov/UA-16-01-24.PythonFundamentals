a = 3
b = 5

def maximum(a, b):
    '''The function to find the
     the largest number of two numbers'''
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return f"Numbers are equal"
    
print(maximum(a, b))


