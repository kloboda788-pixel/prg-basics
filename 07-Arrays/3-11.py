# Returns True if both arrays have the same length
# and the same values at the same indexes
def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

# Prints array elements separated by spaces
def print_array(label, array):
    print(label, end=' ')
    for element in array:
        print(element, end=' ')
    print()

# Prints both arrays and the comparison result
def show_comparison(array1, array2):
    print_array('Array1:', array1)
    print_array('Array2:', array2)
    if compare(array1, array2):
        print('Comparison: arrays are the same')
    else:
        print('Comparison: arrays are different')
    print()

def main():
    show_comparison(["water", "book", "sky"], ["water", "book", "sky"])
    show_comparison([True, False], [True, False, True])
    show_comparison([5, 3, 1], [5, 3, 1])
    show_comparison([3, 2, 1], [3, 2])

if __name__ == "__main__":
    main()