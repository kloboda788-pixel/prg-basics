# Returns True if the text is a valid binary number
def f(binary_number):
    # An empty text is not a number
    if binary_number == '':
        return False
    # If any character is not 0 or 1, the number is invalid
    for char in binary_number:
        if char != '0' and char != '1':
            return False
    # All characters were 0 or 1
    return True

if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))