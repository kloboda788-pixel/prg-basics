numbers = (10, 20, 30, 40, 50)

# [::-1] returns the elements in reverse order (works for tuples and lists)
reversed_numbers = numbers[::-1]

# Print values separated by commas without spaces
print('Tuple:', end=' ')
for i in range(len(numbers)):
    if i > 0:
        print(',', end='')
    print(numbers[i], end='')
print()

print('Reverse order:', end=' ')
for i in range(len(reversed_numbers)):
    if i > 0:
        print(',', end='')
    print(reversed_numbers[i], end='')
print()