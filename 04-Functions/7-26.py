# Returns the text with all characters separated by a dash
def f(text):
    result = ''
    for i in range(len(text)):
        # Add a dash before every character except the first one
        if i > 0:
            result += '-'
        result += text[i]
    return result

if __name__ == "__main__":
    print(f("University"))
    print(f("UE"))
    print(f("x"))
    print(f(""))