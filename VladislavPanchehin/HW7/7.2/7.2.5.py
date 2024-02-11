def reversed(st):
    #Breaking a string into words
    text = st.split()
    #Changing the word order
    reverse_text = text[::-1]
    #Combining words into a string
    combining_words = ' '.join(reverse_text)
    return combining_words



print(reversed('Hi There.'))  # 'There. Hi')
