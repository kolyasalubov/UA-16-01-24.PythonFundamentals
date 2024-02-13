#  CODEWARS FOR 7 HW
# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

# # Simple: Find The Distance Between Two Points

import math
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)2 + (y2 - y1)2)
    rounded_distance = round(distance, 2)
    return rounded_distance

# # No yelling!
def filter_words(st):
    adjusted_string = " ".join(st.split())
    adjusted_string = adjusted_string.capitalize()
    return adjusted_string

# # Convert a Number to a String - 
def number_to_string(num):
    stringed_num = str(num)
    return stringed_num

# Reversing Words in a String - 

def reverse(st):
    string_to_list = st.split()
    reversed_list = string_to_list[::-1]
    return " ".join(reversed_list)


# Reverse List Order
def reverse_list(l):
    reversed = l[::-1]
    return reversed

# Multiples of 3 or 5 

def solution(number):
    if number < 0:
        return 0
    else:
        num = sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
        return num
    
# Will you make it? 

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    return False

# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name and name[0].lower() == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"

# Convert boolean values to strings 'Yes' or 'No’ - 
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Counting sheep -
def count_sheeps(sheep):
    sheep_counter = 0
    for sheep_status in sheep:
        if sheep_status:
            sheep_counter += 1
    return sheep_counter

# Is this my tail?
def correct_tail(body, tail):
    return True if tail == body[-1] else False