###
# Parking meter: calculates the parking fee
# 1-2 hours: 5 PLN, 3-6 hours: 15 PLN, over 6 hours: 20 PLN
#
hours = int(input('Enter the number of parking hours: '))
if hours < 1:
    print('Invalid number of hours')
else:
    if hours <= 2:
        fee = 5
    elif hours <= 6:
        fee = 15
    else:
        fee = 20
    print(f'Parking fee: {fee} PLN')