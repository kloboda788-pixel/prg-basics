# Returns the value of an expression with single-digit numbers, e.g. "2+3-4"
def f(expression):
    # Start with the first digit
    result = int(expression[0])
    # Operators are at odd indexes (1, 3, 5, ...), so the step is 2
    for i in range(1, len(expression), 2):
        operator = expression[i]
        # The digit is right after the operator
        digit = int(expression[i + 1])
        if operator == '+':
            result += digit
        else:
            result -= digit
    return result

if __name__ == "__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))