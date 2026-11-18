# Returns the sentence without spaces
def f(sentence):
    result = ''
    # Copy every character except spaces
    for char in sentence:
        if char != ' ':
            result += char
    return result

if __name__ == "__main__":
    print(f("integrated development environment"))
    print(f("A programming language is a system of notation for writing computer programs"))