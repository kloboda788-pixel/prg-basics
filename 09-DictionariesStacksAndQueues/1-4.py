###
# Operations on a dictionary with values of different types
#
person = {
    "name": "Marek",                     # str
    "surname": "Banach",                 # str
    "age": 25,                           # int
    "hobby": ["swimming", "excursions"], # list
    "married": True,                     # bool
    "phone": {"landline": "123444321", "mobile": "777888999"}  # dict (dictionary in a dictionary)
}

# 1. Displays name - a value is read by its key in square brackets
print('Name:', person["name"])

# 2. Displays hobby
print('Hobby:', person["hobby"])

# 3. Displays the entire contents of the dictionary
print(person)

# 4. Changes surname - assigning to an existing key replaces the value
person["surname"] = "Nowak"

# 5. Changes person's marriage status - 'not' turns True into False
person["married"] = not person["married"]

# 6. Adds gender - assigning to a new key adds a new pair
person["gender"] = "male"

# 7. Adds a new hobby - the value is a list, so append() works on it
person["hobby"].append("bicycle")

# 8. Adds work phone - the value is a dictionary, so a new key is added inside it
person["phone"]["work"] = "313131444"

# 9. Displays the entire contents of the dictionary (iterate over items)
print()
for key, value in person.items():
    print(f'{key}: {value}')