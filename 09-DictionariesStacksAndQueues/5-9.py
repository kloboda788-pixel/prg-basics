###
# Counts registered cars from each province of Poland
#
import csv

# Returns a dictionary: first letter -> province name
def read_provinces(file_name):
    provinces = {}
    # encoding='utf-8' - province names contain Polish characters
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # skip the header line
        for row in reader:
            letter = row[0]
            name = row[1]
            provinces[letter] = name
    return provinces

# Returns a dictionary: first letter -> number of cars
def count_cars(file_name):
    counts = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            registration = line.strip()
            if registration == '':
                continue
            letter = registration[0]
            # get(letter, 0) returns 0 when the letter is not in the dictionary yet
            counts[letter] = counts.get(letter, 0) + 1
    return counts

def main():
    provinces = read_provinces('province.csv')
    counts = count_cars('vehicle.txt')

    print('CARS BY PROVINCE')
    for letter, name in provinces.items():
        print(f'{name:<20} {counts.get(letter, 0)}')

if __name__ == "__main__":
    main()