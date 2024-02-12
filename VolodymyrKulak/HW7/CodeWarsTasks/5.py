
#V. Reversing Words in a String
def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)
