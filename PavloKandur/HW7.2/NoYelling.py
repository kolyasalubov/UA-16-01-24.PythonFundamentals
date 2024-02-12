def filter_words(st):
    list_of_words = st.split()
    correct_string = ''
    for i in list_of_words:
        correct_string += i.lower()
        if i != list_of_words[len(list_of_words) - 1]:
            correct_string += ' '
    return  correct_string.capitalize()
