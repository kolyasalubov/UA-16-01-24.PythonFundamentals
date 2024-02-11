#Task 1
def greet(name):
    
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    



#Task 2
def distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return round(distance, 2)
    


#Task 3
def filter_words(st):
    return ' '.join([st.split()[0].capitalize()] + [word.lower() for word in st.split()[1:]])



#Task4
def number_to_string(num):
    if num == 0:
        return "0"

    is_neg = num < 0
    num = abs(num)
    res = ""

    while num > 0:
        digit = num % 10
        res = chr(ord('0') + digit) + res
        num //= 10

    if is_neg:
        res = "-" + res

    return res

#Task 5
def reverse(st):
    words = [word for word in st.split() if word]
    st = ' '.join(words[::-1])

    return st



#Task 6
def reverse_list(l):
  return l[::-1]



#Task 7
def solution(number):
    if number < 0:
        return 0

    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum



#Task 8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = fuel_left * mpg
    
    if max_distance >= distance_to_pump:
        return True
    else:
        return False
    


#Task 9
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    


#Task 10
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else: 
        return "No"
    


#Task 11
def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s:
            count += 1
    return count



#Task12 
def correct_tail(body, tail):
    sub = body[-len(tail):]
    if sub == tail:
        return True
    else:
        return False