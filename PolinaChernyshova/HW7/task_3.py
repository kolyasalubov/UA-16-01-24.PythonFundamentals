
def calculate_char_to_dict(word: str)->dict:
    '''
    The function takes to str type argument: word
    Create a dict
    Makes dict.keys with word letters 
    Makes dict.values with amount of letters in word (str)
    Return the dict
    '''

    dict_word = {x: word.count(x) for x in word}

    # second variant without function
    # dict_word = {}
    # for i in word:
    #     if i in dict_word:
    #         continue
    #     dict_word[i] = dict_word.get(i, 0)
    #     for x in word:
    #         if  i == x:
    #             dict_word[i] = dict_word[i] + 1

    return dict_word


user_word = input("Enter word for count letters: ")

print(calculate_char_to_dict(user_word))
