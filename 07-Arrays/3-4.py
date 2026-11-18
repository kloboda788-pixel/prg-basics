numbers = [15, 8, 31, 47, 2, 19]

print('existed array:', end=' ')
for number in numbers:
    print(number, end=' ')
print()

print('reverse array:', end=' ')
# range(start, stop, step): from the last index down to 0, step -1
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=' ')
print()