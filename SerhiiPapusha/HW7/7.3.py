word = "famousadao"

def check_qnt_char(text_input):
    output = {}
    for char in text_input:
        qnt = text_input.count(char)
        output[char] = qnt
    return output

print(check_qnt_char(word))