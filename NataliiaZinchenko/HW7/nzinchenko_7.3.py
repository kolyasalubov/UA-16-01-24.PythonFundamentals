# Creating a function which calculates the number of characters included in given string

def calculate_number_of_characters(input_string):
    '''Function that returns the number of characters in entered user's string
       input_string: str
    '''
    letters_list = []
    counting_dict = {}
    for letter in input_string:
        letters_list.append(letter)


    for letters_list_element in letters_list:
        if letters_list_element not in counting_dict.keys():
            counting_dict[letters_list_element] = 1
        elif letters_list_element in counting_dict.keys():
            counting_dict.update({letters_list_element: counting_dict[letters_list_element] + 1}) 


    return counting_dict


print(calculate_number_of_characters("hello"))
