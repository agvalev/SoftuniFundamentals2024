def lenght_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def charachters_are_valid(name):
    for charachter in name:
        if not (charachter.isalnum() or charachter == "-" or charachter == "_"):
            return False
    return True


def no_redundant_symbolds(name):
    if " " in name:
        return False
    return True


def is_valid(name):
    if lenght_is_valid(name) and charachters_are_valid(name) and no_redundant_symbolds(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if is_valid(username):
        print(username)
