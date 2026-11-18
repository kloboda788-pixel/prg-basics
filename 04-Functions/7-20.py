# Helper function: returns True if the number is prime
def is_prime(number):
    if number < 2:
        return False
    # If any smaller number divides it, it is not prime
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

# Returns the n-th prime number
def f(n):
    # How many primes have been found so far
    counter = 0
    number = 1
    # Check the next numbers until the n-th prime is found
    while counter < n:
        number += 1
        if is_prime(number):
            counter += 1
    return number

if __name__ == "__main__":
    print(f(1))
    print(f(5))