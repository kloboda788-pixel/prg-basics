###
# Prints the text from a file and counts its words
#
words = 0
with open('pets.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end="")
        # split() divides the line into a list of words
        words += len(line.split())

print()
print('Number of words:', words)