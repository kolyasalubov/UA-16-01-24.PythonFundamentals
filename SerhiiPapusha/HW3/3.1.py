zen_of_python = '''Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!'''


better_count = zen_of_python.count("better")
never_count = zen_of_python.count("never")
is_count = zen_of_python.count("is")

print(f'''\tWord "better" occures {better_count} times\n
      Word "never" occures {never_count} times\n
      Word "is" occures {is_count} times''')
print("---------------------------\n\n\n\n")
uppercase_zen = zen_of_python.upper()
print(uppercase_zen)
print("---------------------------\n\n\n\n")
replace_zen = zen_of_python.replace('i', '&')
print(replace_zen)
print("---------------------------\n\n\n\n")