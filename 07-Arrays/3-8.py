numbers = [15, 8, 31, 47, 2, 19]

# Add all values with a while loop
total = 0
i = 0
while i < len(numbers):
    total += numbers[i]
    i += 1

mean = total / len(numbers)

print('Array:', numbers)
print(f'Arithmetic mean: {mean:.2f}')