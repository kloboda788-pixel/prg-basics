import json

###
# Prints a summary of hotel reservations
#

# Returns the list of reservations from the JSON file
def read_reservations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # the file contains a dictionary with one key: "reservations"
    return data['reservations']

# Returns the value of one reservation
def reservation_value(reservation):
    return reservation['nights'] * reservation['price_per_night']

# Returns the number of different rooms
def count_rooms(reservations):
    rooms = set()
    for reservation in reservations:
        # a set keeps every room number only once
        rooms.add(reservation['room_number'])
    return len(rooms)

# Returns the number and the total value of reservations with the given paid status
def summary(reservations, paid):
    count = 0
    total = 0
    for reservation in reservations:
        if reservation['paid'] == paid:
            count += 1
            total += reservation_value(reservation)
    return count, total

def main():
    reservations = read_reservations('reservations.json')
    paid_count, paid_total = summary(reservations, True)
    unpaid_count, unpaid_total = summary(reservations, False)

    print('Number of rooms:', count_rooms(reservations))
    print('Number of paid reservations:', paid_count)
    print('Number of unpaid reservations:', unpaid_count)
    print(f'Total value of paid reservations: {paid_total:.2f}')
    print(f'Total value of unpaid reservations: {unpaid_total:.2f}')

if __name__ == "__main__":
    main()