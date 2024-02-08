def counter_symbols(text):
    count_symbol = {}
    for symbol in text:
        if symbol in count_symbol:
            count_symbol[symbol] += 1
        else:
            count_symbol[symbol] = 1
    return count_symbol


print(counter_symbols('hello'))

