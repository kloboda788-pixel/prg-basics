n = int(input('How many prime numbers? N = '))
found = 0
candidate = 2

print('Prime numbers:', end=' ')
while found < n:
    is_prime = True
    divisor = 2
    while divisor < candidate:
        if candidate % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(candidate, end=' ')
        found += 1
    candidate += 1
print()