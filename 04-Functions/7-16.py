# Returns the n-th value of the Fibonacci sequence (0, 1, 1, 2, 3, 5, ...)
def f(n):
    # The first two values of the sequence
    a = 0
    b = 1
    # Move forward n - 1 times: the next value is the sum of the previous two
    for i in range(n - 1):
        temp = a + b
        a = b
        b = temp
    return a

if __name__ == "__main__":
    print(f(5))
    print(f(9))