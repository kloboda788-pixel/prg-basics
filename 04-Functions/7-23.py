# Returns True if the password has at least 6 characters
# and every character appears only once
def f(password):
    if len(password) < 6:
        return False
    # If any character appears more than once, the password is invalid
    for char in password:
        if password.count(char) > 1:
            return False
    return True

if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))