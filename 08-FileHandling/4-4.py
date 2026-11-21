###
# Prints the file five lines at a time
#
file_name = 'it_company.csv'
lines_per_page = 5

with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# i = 0, 5, 10, ... - the first line of each page
for i in range(0, len(lines), lines_per_page):
    # slicing: lines from i to i + 5 (without i + 5)
    for line in lines[i:i + lines_per_page]:
        print(line, end="")
    # wait for the Enter key, but not after the last page
    if i + lines_per_page < len(lines):
        input('Press Enter key...')