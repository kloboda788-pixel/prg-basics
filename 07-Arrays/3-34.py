# Prints a 2D array in rows and columns
def print_array(array):
    for row in array:
        for value in row:
            print(f'{value:2}', end=' ')
        print()

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print('Before:')
print_array(array)

# Swap the first row (index 0) and the last row (index -1)
temp = array[0]
array[0] = array[-1]
array[-1] = temp

print('After:')
print_array(array)