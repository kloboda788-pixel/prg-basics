# Returns the sum 1 + 2 + ... + n using recursion
def sum_natural(n):
    # Stop condition: the sum of numbers from 1 to 1 is 1
    if n == 1:
        return 1
    # sum(n) = n + sum(n-1)
    return n + sum_natural(n - 1)

if __name__ == "__main__":
    print(f'Sum of natural numbers <1,10>: {sum_natural(10)}')