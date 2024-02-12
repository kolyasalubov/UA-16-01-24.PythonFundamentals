
def letter_counter(words: str) -> dict:
    """
    This func counts the letters in a string
    :param words: str
    :return: dict with counted letters from the entered string
    """
    letters_dict = {}

    for item in words:
        if item in letters_dict:
            letters_dict[item] += 1
        else:
            letters_dict[item] = 1

    return letters_dict


words = str(input("Enter a word/s to count letters in: "))
print(letter_counter(words))
