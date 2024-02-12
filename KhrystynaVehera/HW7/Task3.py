word_to_count = input("Please write a word to calculate letters: ")


def letters_counter(word_to_count):
    letters_dict = dict()

    for i in set(word_to_count):
        letters_dict[i] = word_to_count.count(i)

    return letters_dict  

print(letters_counter(word_to_count))