# Returns the acronym - first letters of all words
def f(name):
    result = ''
    # split() divides the text into a list of words
    for word in name.split():
        # Take the first letter of each word
        result += word[0]
    return result

if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))