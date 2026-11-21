###
# Records voting results in a JSON file
#
import json

file_name = 'voting.json'

# Read the contents of the json file
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        # json.load() changes the file content into a dictionary
        votes = json.load(file)
except FileNotFoundError:
    # the first run - there is no file yet, so start with an empty dictionary
    votes = {}

# Vote for a person
person_name = input('Name of the person you are voting for: ')
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

# Save voting data to json file
with open(file_name, 'w', encoding='utf-8') as file:
    # json.dump() writes the dictionary to the file; indent=4 makes it readable
    json.dump(votes, file, indent=4)

print('Current results:')
for name, count in votes.items():
    print(f'{name}: {count}')