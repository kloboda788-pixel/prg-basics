# Returns the result of the operation given as a text
def f(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    else:
        # Unknown operator
        return None

if __name__ == "__main__":
    print(f(2, 3, "+"))
    print(f(2, 3, "%"))
    print(f(2, 3, "**"))
    print(f(2, 3, "*"))
    print(f(2, 3, "-"))