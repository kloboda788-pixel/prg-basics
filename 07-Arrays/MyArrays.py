# Module with functions operating on an array of numbers.
# Built-in functions (max, min, sorted, sum) are not used.

# Helper: returns a sorted copy of the array (Bubble Sort)
def sort_copy(array):
    # Copy the elements, so the original array is not changed
    result = []
    for element in array:
        result.append(element)
    n = len(result)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp
    return result

# Returns a two-element array: [smallest, largest]
def min_max(array):
    smallest = array[0]
    largest = array[0]
    for element in array:
        if element < smallest:
            smallest = element
        if element > largest:
            largest = element
    return [smallest, largest]

# Returns the second largest element
def second_largest(array):
    sorted_array = sort_copy(array)
    # After sorting, the second largest is the second from the end
    return sorted_array[len(sorted_array) - 2]

# Returns the difference between the largest and the smallest value
def difference(array):
    values = min_max(array)
    return values[1] - values[0]

# Returns the median - the middle value of the sorted numbers
def median(array):
    sorted_array = sort_copy(array)
    n = len(sorted_array)
    middle = n // 2
    if n % 2 == 1:
        # Odd number of elements - one middle value
        return sorted_array[middle]
    else:
        # Even number of elements - mean of the two middle values
        return (sorted_array[middle - 1] + sorted_array[middle]) / 2

# Returns array elements as a string separated by the given sign
def to_string(array, separator='-'):
    result = ''
    for i in range(len(array)):
        if i > 0:
            result += separator
        result += str(array[i])
    return result