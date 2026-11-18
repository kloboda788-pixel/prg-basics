# Sorts the array in ascending order using Bubble Sort
def bubblesort(array):
    n = len(array)
    # Each pass moves the largest remaining value to the end
    for i in range(n):
        # The last i elements are already sorted
        for j in range(n - i - 1):
            # Swap neighbours if they are in the wrong order
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

def main():
    print(bubblesort([5, 3, 8, 1, 9, 2]))
    print(bubblesort([10, -4, 7, 0, 3]))
    print(bubblesort([100, 50, 75, 25]))

if __name__ == "__main__":
    main()