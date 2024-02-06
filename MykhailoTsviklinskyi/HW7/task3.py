def calculate_characters_number(query: str)->dict:
    """
    This function converts given query to character list
    and counts the number of each character
    """
    list_from_query = list(query)

    dictionary_of_characters = {}
    
    for item in list_from_query:
        dictionary_of_characters.update({item: list_from_query.count(item)})
    return dictionary_of_characters

string_from_customer = (input("Please enter some text: ")).replace(' ', '')

print(f"Number of characters from given string {calculate_characters_number(string_from_customer)}")
