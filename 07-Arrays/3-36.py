# Returns an n x n identity matrix: 1 on the main diagonal, 0 elsewhere
def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            # Row number equal to column number = main diagonal
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

# Prints a 2D array in rows and columns
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()

def main():
    for size in [3, 5, 8]:
        print(f'Identity matrix {size}x{size}:')
        print_matrix(identity_matrix(size))
        print()

if __name__ == "__main__":
    main()