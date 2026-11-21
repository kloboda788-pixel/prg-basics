import json

###
# Prints information about cities from a JSON file
#

# Open the JSON file in read mode
# encoding='utf-8' - city names contain Polish characters
with open('cities.json', 'r', encoding='utf-8') as file:
    # Load the data - this file contains a list of dictionaries
    data = json.load(file)

# Print the JSON data
for city in data:
    # every city is one dictionary
    for key, value in city.items():
        print(key, ':', value)
    print()