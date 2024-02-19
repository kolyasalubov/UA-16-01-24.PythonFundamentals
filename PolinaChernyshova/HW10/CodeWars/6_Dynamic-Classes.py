def class_name_changer(cls, new_name):

    if new_name[0] != new_name[0].upper():
        raise Exception('error')
    elif not new_name.isalnum():
        raise Exception('error')
    elif new_name[0].isnumeric():
        raise Exception('error')
    cls.__name__ = new_name