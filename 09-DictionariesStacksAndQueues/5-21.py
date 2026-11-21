import json

###
# Writes data about a favourite movie to a JSON file
#
favourite = {
    "title": "The Matrix",
    "year": 1999,
    "directors": ["Lana Wachowski", "Lilly Wachowski"],
    "genre": "Science Fiction",
    "lead_actor": "Keanu Reeves",
    "duration_min": 136,
    "watched": True
}

with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(favourite, file, indent=4)

print('Data has been written to favourite.json')