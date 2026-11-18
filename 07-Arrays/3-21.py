numbers = [2.5, 7.1, 3.8, 9.4, 1.2, 6.6, 4.9]

print('Array:', numbers)
value = float(input('Value: '))

# Count elements greater than the given value
counter = 0
for number in numbers:
    if number > value:
        counter += 1

print(f'Number of elements greater than {value}: {counter}')