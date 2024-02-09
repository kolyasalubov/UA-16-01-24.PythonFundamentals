# Reversing Words in a String
# https://www.codewars.com/kata/reversing-words-in-a-string

def reverse(st):
    return " ".join(st.split()[::-1])
