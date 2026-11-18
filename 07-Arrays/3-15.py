# Returns True if the number is present in the array
def occurs(number, array):
    for element in array:
        if element == number:
            return True
    return False

def main():
    array = [15, 38, 7, 23, 14]
    number = int(input('Number: '))

    print('Array:', end=' ')
    for element in array:
        print(element, end=' ')
    print()

    if occurs(number, array):
        print(f'Result: number {number} appears in the array')
    else:
        print(f'Result: number {number} does not appear in the array')

if __name__ == "__main__":
    main()