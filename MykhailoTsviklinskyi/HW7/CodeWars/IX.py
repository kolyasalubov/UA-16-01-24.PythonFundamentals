# Are You Playing Banjo?
# https://www.codewars.com/kata/are-you-playing-banjo

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    