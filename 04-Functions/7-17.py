# Returns True if the text reads the same backwards
def f(palindrome):
    # [::-1] returns the text in reverse order
    return palindrome == palindrome[::-1]

if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))