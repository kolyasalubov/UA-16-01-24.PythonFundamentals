# Creating a function which calculates the number of characters included in given string

def calculate_number_of_characters(input_string):
    '''Function that returns the number of characters in entered user's string
       input_string: str
    '''
    letters_list = []
    counting_list = []
    counting_dict = {}
    for letter in input_string:
        letters_list.append(letter)
    
    for letters_list_element in letters_list:
        counter = 0
        if letters_list_element not in letters_list:
            counter = 1
            counting_dict.update(f"{letters_list_element}: {counter}")
        else:
            counter += 1
            counting_dict.update(f"{letters_list_element}: {counter}")


    return counting_dict

print(calculate_number_of_characters("hello"))
