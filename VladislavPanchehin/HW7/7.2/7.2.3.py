def filter_words(st):
    capitalize_string = st.capitalize()
    clean_backspace  = ' '.join(capitalize_string.split())
    return clean_backspace

print(filter_words('This    will    not    pass '))# 'This will not pass')