def count_characters(input_string):
    
    """Calculate the number of characters in the given string and return a dictionary with character's count"""
    character_count = {}

    for character in input_string:
        if character in character_count:
            character_count[character] = character_count[character] + 1
        else:
            character_count[character] = 1

    return character_count


input_string = "hello"
result = count_characters(input_string)
print(result)



