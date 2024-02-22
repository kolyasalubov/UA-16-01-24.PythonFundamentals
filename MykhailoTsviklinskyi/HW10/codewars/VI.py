# Dynamic Classes
# https://www.codewars.com/kata/55ddb0ea5a133623b6000043

# import string

# def class_name_changer(cls, new_name):

#     if new_name[0] not in string.ascii_uppercase:
#         raise Exception("Name has to start with uppercase letter")
    
#     if new_name[0] not in string.digits:
#         raise Exception("Name has to start with uppercase letter")
    
#     for item in new_name:
#         if item not in string.ascii_letters and item in string.punctuation:
#             raise Exception("Allow only names with alphanumeric chars")

#     cls.__name__ = new_name


a = " Test!"
print(list(a))
# print(list(string.ascii_uppercase))


# if a[0] in string.ascii_uppercase:
#     print(True)
# else:
#     raise Exception(False)


# b = a[0].isupper()

# print(b)


# def class_name_changer(cls, new_name):

#     if new_name[0] != new_name[0].upper():
#         raise Exception('error')
#     elif not new_name.isalnum():
#         raise Exception('error')
#     elif new_name[0].isnumeric():
#         raise Exception('error')
#     cls.__name__ = new_name