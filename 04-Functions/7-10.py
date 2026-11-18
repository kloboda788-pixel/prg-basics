# Returns the number of negative even numbers in the range <x, y>
def f(x, y):
    counter = 0
    # y + 1, because range() does not include the end value
    for n in range(x, y + 1):
        if n < 0 and n % 2 == 0:
            counter += 1
    return counter

if __name__ == "__main__":
    print(f(-7, 8))
    print(f(-1, 11))