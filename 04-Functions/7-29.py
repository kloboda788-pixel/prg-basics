# Calculates the factorial recursively (the function calls itself)
def factorial(n):
    # 0! = 1, 1! = 1 - the stop condition
    if n == 0 or n == 1:
        return 1
    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # 5! = 5 * 4 * 3 * 2 * 1 = 120
    print(f'5! = {factorial(5)}')