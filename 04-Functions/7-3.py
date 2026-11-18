# Import the module with the month() function
import months

def main():
    n = int(input('Enter month number: '))
    # The function is called with the module name prefix
    print(f'The name of month {n} is {months.month(n)}')

if __name__ == "__main__":
    main()