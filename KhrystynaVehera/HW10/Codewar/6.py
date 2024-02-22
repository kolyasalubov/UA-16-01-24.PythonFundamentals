def class_name_changer(self, name):
    if name[0].isupper() and name.isalnum():
        self.__name__ = name
    else:
        return Error