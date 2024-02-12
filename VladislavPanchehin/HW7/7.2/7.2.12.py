def correct_tail(body, tail):
    # match checking
    if body[-1] == tail:
        return True
    else:

        return False

# variant 2


def correct_tail(body, tail):
    return body.endswith(tail)
