# Returns True if all elements of the first array appear in the second array
def is_subset(array1, array2):
    for element in array1:
        if element not in array2:
            # One missing element is enough to answer False
            return False
    return True

def main():
    array1 = [3, 7, 1]
    array2 = [1, 5, 3, 9, 7]
    print('Array1:', array1)
    print('Array2:', array2)
    print('Array1 is a subset of Array2:', is_subset(array1, array2))

    array3 = [3, 4]
    print('Array3:', array3)
    print('Array3 is a subset of Array2:', is_subset(array3, array2))

if __name__ == "__main__":
    main()