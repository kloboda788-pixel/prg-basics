names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

# Start with the first name as the longest one
longest_name = names[0]
for name in names:
    # Compare the lengths (number of characters)
    if len(name) > len(longest_name):
        longest_name = name

print('Names:', end=' ')
for name in names:
    print(name, end=' ')
print()
print('Longest name:', longest_name)