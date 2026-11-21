###
# Reads from file, line by line, and numbers the lines
#
with open('countries.txt', 'r', encoding='utf-8') as file:
    number = 1
    for line in file:
        # end="" - the line already ends with a newline character
        print(f'{number}. {line}', end="")
        number += 1
# The last line of the file has no newline character, so finish the line
print()