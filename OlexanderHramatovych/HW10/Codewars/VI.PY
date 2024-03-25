def class_name_changer(cls, new_name):

    if new_name[0] == new_name[0].upper() and new_name.isalnum()==True and new_name[0].isnumeric() == False:
        cls.__name__ = new_name