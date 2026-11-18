array = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Each cell = (row number) * (column number), counting from 1
for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = (i + 1) * (j + 1)

for row in array:
    for value in row:
        # :2 - every number takes 2 characters, so the columns are aligned
        print(f'{value:2}', end=' ')
    print()