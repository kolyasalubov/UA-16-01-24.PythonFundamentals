# Text that should be worked with

python_philosophy='''
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
'''


# First task
count_of_better = str(python_philosophy.count('better')) # converting to str
count_of_never = str(python_philosophy.count('never'))
count_of_is = str(python_philosophy.count('is'))

print('Number of the word "better" is: ' + count_of_better)
print('Number of the word "better" is: '+count_of_never)
print('Number of the word "better" is: '+count_of_is)


# Second task
upper_case = python_philosophy.upper()
print(upper_case)


# Third task
replace = python_philosophy.replace('i','&')
print(replace)