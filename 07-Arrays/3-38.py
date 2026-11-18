# Converts a 2D array into a 1D array (all rows one after another)
def to_1d(array_2d):
    result = []
    for row in array_2d:
        for value in row:
            result.append(value)
    return result

def main():
    arrays = [
        [[2, 3], [1, 5]],
        [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
        [[2, 1], [3, 5], [7, 4], [2, 6]]
    ]
    for array in arrays:
        print(array, '->', to_1d(array))

if __name__ == "__main__":
    main()