# Returns n asterisks as a string
def star(n):
    # '*' * n repeats the asterisk n times
    return '*' * n

def main():
    numbers = [2, 6, 4, 9, 7]
    for number in numbers:
        print(f'{number}: {star(number)}')

if __name__ == "__main__":
    main()