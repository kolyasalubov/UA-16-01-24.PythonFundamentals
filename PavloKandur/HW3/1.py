Zen_of_py ="""Beautiful is better than ugly.
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
In the face of ambiguity, refuse the temptation to guess.\
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
list_of_words=Zen_of_py.split()
better_counter = 0
never_counter = 0
is_counter = 0
for i in list_of_words:
    if i == "better" or "better.":
        better_counter += 1
    if i == "never" or i == "never.":
        never_counter += 1
    if i == "is" or i == "is.":
        is_counter += 1
print(f'There are:\n{better_counter} better,\n{never_counter} never,\n{is_counter} is,\nin the text.\n')
changed_zen = Zen_of_py.replace("i", "&")
changed_zen_v2 = changed_zen.upper()

for i in changed_zen_v2:
    print(i,end='')
    if i =='.':
        print()

