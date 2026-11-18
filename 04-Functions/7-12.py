# Returns n asterisks separated by slashes, e.g. "*/*/*"
def f(n):
    result = ''
    for i in range(n):
        # Add a slash before every asterisk except the first one
        if i > 0:
            result += '/'
        result += '*'
    return result

if __name__ == "__main__":
    print(f(4))
    print(f(1))