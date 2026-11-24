###
# Class with basic statistics of a set of numbers
#
class Statistics:
    def __init__(self):
        # the numbers are stored in an array (list)
        self.numbers = []

    # 1. Adds the next number read from the keyboard
    def add_number(self):
        number = float(input('Enter a number: '))
        self.numbers.append(number)

    # 2. Displays all numbers separated by a space
    def display_numbers(self):
        # :g - prints 12.0 as 12, but keeps 12.5 as 12.5
        print('Numbers:', ' '.join(f'{n:g}' for n in self.numbers))

    # 3. Returns the greatest number
    def maximum(self):
        return max(self.numbers)

    # 4. Returns the smallest number
    def minimum(self):
        return min(self.numbers)

    # 5. Returns the arithmetic mean
    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    # 6. Returns the median - the middle value of the sorted numbers
    def median(self):
        values = sorted(self.numbers)
        n = len(values)
        middle = n // 2
        if n % 2 == 1:
            return values[middle]
        return (values[middle - 1] + values[middle]) / 2

    # 7. Prints all calculated statistics
    def print_statistics(self):
        print(f'Minimum: {self.minimum():g}')
        print(f'Maximum: {self.maximum():g}')
        print(f'Arithmetic mean: {self.mean():.2f}')
        print(f'Median: {self.median():g}')


def main():
    stats = Statistics()
    # the task gives 5 numbers: 12, 37, 6, 9, 17
    for i in range(5):
        stats.add_number()
    stats.display_numbers()
    stats.print_statistics()

if __name__ == "__main__":
    main()