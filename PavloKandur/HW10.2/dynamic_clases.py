import re
def class_name_changer(cls, new_name):
    pattern = re.compile(r'[^a-zA-Z0-9\s\.,!@#\$%\^&\*\(\)\-_\+=\[\]\{\}\|;:"\'<>\?\/]')
    if new_name[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if not pattern.search(new_name):
            cls.__name__ = new_name
    else:
        raise Exception("Not valid name")