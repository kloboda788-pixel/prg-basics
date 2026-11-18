# Returns the sum of digits that appear more than once in the number
def f(number):
    digits = str(number)
    total = 0
    for char in digits:
        # count() tells how many times the digit appears in the whole number
        if digits.count(char) > 1:
            total += int(char)
    return total

if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))