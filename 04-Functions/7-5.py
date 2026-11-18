# Import the module with the in_range() function
import ranges

def main():
    number = int(input('A number: '))
    # Range limits
    x = 2
    y = 15
    # Change the boolean result into 'yes' / 'no' text
    if ranges.in_range(number, x, y):
        answer = 'yes'
    else:
        answer = 'no'
    print(f'Number {number} in the range <{x},{y}>: {answer}')

if __name__ == "__main__":
    main()