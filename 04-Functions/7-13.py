# Returns numbers from 1 to n joined into one text
def f(n):
    result = ''
    for i in range(1, n + 1):
        # A number must be changed into text before joining
        result += str(i)
    return result

if __name__ == "__main__":
    print(f(11))
    print(f(4))