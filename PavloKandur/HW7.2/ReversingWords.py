def reverse(st):
    list_of_words = st.split()
    new_st = ''
    i = len(list_of_words) - 1
    for _ in list_of_words:
        new_st += list_of_words[i]
        if i != 0:
            new_st += ' '
        i-=1
    return new_st