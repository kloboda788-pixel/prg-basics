###
# Reads the entire contents of a file
#
def read_from_file(name):
    with open(name, encoding='utf-8') as file:
        content = file.read()
    return content

# reads the entire file and splits lines into array
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

# calculates the total number of cars parked
total = 0
for line in file_lines:
    # every line is a text, so it must be changed into a number
    total += int(line)

print('Total cars parked:', total)