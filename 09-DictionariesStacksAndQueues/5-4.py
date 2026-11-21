###
# Calculates the total number of hours in a semester
#
winter_semester = {
    "math": 60,
    "programming": 30,
    "history": 15
}

total = 0
# values() returns only the values (hours), without the keys
for hours in winter_semester.values():
    total += hours

print(f'The total number of hours in the winter semester is {total}')