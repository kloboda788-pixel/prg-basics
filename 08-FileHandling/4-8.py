###
# Prints file names with an extension of exactly 4 characters
#
import re

# \. - a dot (a plain dot in regex means "any character")
# [a-zA-Z0-9]{4} - exactly 4 letters or digits
# $ - end of the text, so nothing can follow the extension
pattern = r'\.[a-zA-Z0-9]{4}$'

with open('files.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # strip() removes the newline character at the end of the line
        file_name = line.strip()
        if re.search(pattern, file_name):
            print(file_name)