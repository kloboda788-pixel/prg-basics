###
# Compares average hotel prices in two cities
#
hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]

# Returns hotel names separated by commas
def hotel_list(hotels):
    names = []
    for hotel in hotels:
        names.append(hotel["name"])
    return ','.join(names)

# Returns the average room price, rounded to an integer
def avg_price(hotels):
    total = 0
    for hotel in hotels:
        total += hotel["price"]
    return round(total / len(hotels))

def main():
    krakow_avg = avg_price(hotels_in_Krakow)
    sopot_avg = avg_price(hotels_in_Sopot)

    print('Hotels in Krakow:', hotel_list(hotels_in_Krakow))
    print('Average hotel price in Krakow:', krakow_avg)
    print('Hotels in Sopot:', hotel_list(hotels_in_Sopot))
    print('Average hotel price in Sopot:', sopot_avg)

    if krakow_avg < sopot_avg:
        print('Cheaper hotels in: Krakow')
    elif sopot_avg < krakow_avg:
        print('Cheaper hotels in: Sopot')
    else:
        print('Hotels in both cities have the same average price')

if __name__ == "__main__":
    main()