def number_of_chars_in_word(word:str)->dict:
    """
    Name: number_of_chars_in_word
    input parameters: word
    type word: str
    function return dict object
    """
    counted_dict = {}
    for i in word:
        if i in counted_dict.keys():
            continue
        else:
            counted_dict[i] = word.count(i)
    return counted_dict

print(number_of_chars_in_word("abrakadabra"))