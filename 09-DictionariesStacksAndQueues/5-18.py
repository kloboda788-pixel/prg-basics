import json

###
# Prints dogs younger than 5 years
#
with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

print('DOGS YOUNGER THAN 5 YEARS')
for dog in dogs:
    if dog['age'] < 5:
        # JSON true/false become Python True/False
        vaccinated = 'yes' if dog['vaccinated'] else 'no'
        print(f"{dog['name']} ({dog['breed']}), age {dog['age']}, "
              f"{dog['weight_kg']} kg, owner: {dog['owner']}, vaccinated: {vaccinated}")