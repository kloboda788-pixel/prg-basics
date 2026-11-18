# Returns the minimum number of 5, 2 and 1 PLN coins
def f(amount_to_pay):
    coins = 0
    # Use as many 5 PLN coins as possible
    coins += amount_to_pay // 5
    amount_to_pay = amount_to_pay % 5
    # Then as many 2 PLN coins as possible
    coins += amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2
    # The rest (0 or 1) is paid with 1 PLN coins
    coins += amount_to_pay
    return coins

if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))