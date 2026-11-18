# Returns x to the power of n using recursion
def power(x, n):
    # Stop condition: any number to the power of 0 is 1
    if n == 0:
        return 1
    # x^n = x * x^(n-1)
    return x * power(x, n - 1)

if __name__ == "__main__":
    print(f'5^3 = {power(5, 3)}')