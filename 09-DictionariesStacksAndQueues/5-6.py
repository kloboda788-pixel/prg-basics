###
# Merges two dictionaries into one
#
basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

# | joins two dictionaries into a new one (Python 3.9+)
person = basic_data | advanced_data
# another way:
# person = {}
# person.update(basic_data)
# person.update(advanced_data)

for key, value in person.items():
    print(f'{key}: {value}')