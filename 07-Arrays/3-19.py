numbers = (50, 20, 40, 50, 30, 50)

print('Tuple:', end=' ')
for i in range(len(numbers)):
    if i > 0:
        print(',', end='')
    print(numbers[i], end='')
print()

value = int(input('Value: '))

# Count the occurrences with a loop
counter = 0
for number in numbers:
    if number == value:
        counter += 1

print('Number of occurrences:', counter)