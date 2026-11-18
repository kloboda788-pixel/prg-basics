numbers = [34, 7, 19, 4, 21, 8]

even_count = 0
i = 0
# The while loop goes through all indexes: 0, 1, ..., len - 1
while i < len(numbers):
    # A number is even if the remainder of dividing by 2 is 0
    if numbers[i] % 2 == 0:
        even_count += 1
    i += 1

print('Array:', numbers)
print('Number of even values:', even_count)