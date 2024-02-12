# creating function which counts letters in word
def number(word):
    for char in word:      #creating loop for characters
        count = word.count(char) #counting each char
        print(f"{char}:{count}",end=(", ")) # outputting the result
    
number("hello")  #calling the function