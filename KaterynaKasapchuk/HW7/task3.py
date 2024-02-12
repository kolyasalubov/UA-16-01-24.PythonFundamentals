def calculate_characters(word):
    characters = {}
    word = word.lower()
    for character in word:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

word = input("Enter a word: ")

print(calculate_characters(word))