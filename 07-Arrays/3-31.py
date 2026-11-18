# Creates a 2D array with x rows and y columns filled with 0
def create_2d_arr(x, y):
    array = []
    for i in range(x):
        # Every row is a new list with y zeros
        row = []
        for j in range(y):
            row.append(0)
        array.append(row)
    return array

def main():
    array = create_2d_arr(3, 5)
    for row in array:
        for value in row:
            print(value, end=' ')
        print()

if __name__ == "__main__":
    main()