###
# An array (list) of dictionaries
#
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83200000},
    {"name": "France", "population": 67800000},
    {"name": "Spain", "population": 48000000},
    {"name": "Italy", "population": 58900000}
]

# :<9 - the text takes 9 characters, aligned to the left (a column)
print(f'{"COUNTRY":<9}{"POPULATION"}')
# each element of the list is one dictionary
for country in countries:
    print(f'{country["name"]:<9}{country["population"]}')