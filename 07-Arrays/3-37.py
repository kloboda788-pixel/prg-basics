# Returns the transposed matrix: rows become columns
def transpose_matrix(m):
    rows = len(m)
    columns = len(m[0])
    result = []
    # The new matrix has as many rows as the old one had columns
    for j in range(columns):
        new_row = []
        for i in range(rows):
            # Element (i, j) moves to position (j, i)
            new_row.append(m[i][j])
        result.append(new_row)
    return result

# Prints a 2D array in rows and columns
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()

def main():
    matrices = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
        [[5, 6, 7, 8]]
    ]
    for m in matrices:
        print('Matrix:')
        print_matrix(m)
        print('Transposed:')
        print_matrix(transpose_matrix(m))
        print()

if __name__ == "__main__":
    main()