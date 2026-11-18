numbers = [15, 8, 31, 47, 2, 19]

# Add all values with a for loop
total = 0
for number in numbers:
    total += number

mean = total / len(numbers)

print('Array:', numbers)
print(f'Arithmetic mean: {mean:.2f}')