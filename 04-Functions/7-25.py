# Returns the sum of numbers in <x, y> divisible by 2 and 3, but not by 4
def f(x, y):
    total = 0
    for n in range(x, y + 1):
        # % gives the remainder - 0 means "divisible"
        if n % 2 == 0 and n % 3 == 0 and n % 4 != 0:
            total += n
    return total

if __name__ == "__main__":
    print(f(1, 20))
    print(f(10, 30))