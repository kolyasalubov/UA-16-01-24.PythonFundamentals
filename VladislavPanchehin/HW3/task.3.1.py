python_philosophy = """

The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
# logic for the number of occurrences of words

occurrences_better = python_philosophy.count('better')
occurrences_never = python_philosophy.count('never')
occurrences_is = python_philosophy.count('is')

# display all text in uppercase

uppercase_text = python_philosophy.upper()

# replace symbol "i" with "&"

symbol_replace = python_philosophy.replace('i', '&')


# print(type(python_philosophy))
print(f"occurrences of the word - 'better': {occurrences_better}")
print(f"occurrences of the word - 'never': {occurrences_never}")
print(f"occurrences of the word - 'is': {occurrences_is}")
print(uppercase_text)
print(symbol_replace)
