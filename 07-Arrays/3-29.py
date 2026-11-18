# 2 rows, 4 columns
array = [
    [3, 8, 1, 6],
    [9, 2, 7, 4]
]

# Outer loop - rows, inner loop - values in a row
for row in array:
    for value in row:
        print(value, end=' ')
    # New line after each row
    print()