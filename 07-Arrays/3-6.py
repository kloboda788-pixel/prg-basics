numbers = [-15, 8, -31, 47, -2, 19]

# Start with the first element as both the maximum and the minimum
maximum = numbers[0]
minimum = numbers[0]

# Compare every element with the current maximum and minimum
for number in numbers:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

print('Array:', numbers)
print('Maximum:', maximum)
print('Minimum:', minimum)