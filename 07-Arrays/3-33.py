array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Start with the first cell as both the smallest and the largest value
smallest = array[0][0]
largest = array[0][0]
smallest_row, smallest_col = 0, 0
largest_row, largest_col = 0, 0

# Go through every cell and remember its position (row i, column j)
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] < smallest:
            smallest = array[i][j]
            smallest_row, smallest_col = i, j
        if array[i][j] > largest:
            largest = array[i][j]
            largest_row, largest_col = i, j

# + 1, so rows and columns are numbered from 1 for the user
print(f'Smallest value: {smallest} (row {smallest_row + 1}, column {smallest_col + 1})')
print(f'Largest value: {largest} (row {largest_row + 1}, column {largest_col + 1})')