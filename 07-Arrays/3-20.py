import MyArrays

def main():
    numbers = [7, 3, 8, 5, 2]
    smallest_largest = MyArrays.min_max(numbers)

    print('Numbers:', MyArrays.to_string(numbers, ','))
    print('Second largest number:', MyArrays.second_largest(numbers))
    print('Difference between largest and smallest:', MyArrays.difference(numbers))
    print('Median:', MyArrays.median(numbers))
    print('Smallest and largest number:', MyArrays.to_string(smallest_largest, ','))
    print('Numbers as a string:', MyArrays.to_string(numbers))

if __name__ == "__main__":
    main()