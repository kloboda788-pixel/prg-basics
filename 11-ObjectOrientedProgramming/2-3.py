###
# Class describing a taxi ride
#
class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    # Calculates the fare and stores it in the object
    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    # Prints a receipt with all information about the ride
    def print_receipt(self):
        print('TAXI RECEIPT')
        print('------------')
        print(f'Distance: {self.distance} km')
        print(f'Rate:     €{self.rate_per_km:.2f} per km')
        print(f'Fare:     €{self.fare:.2f}')
        print()


def main():
    # two objects - two different rides with different rates
    ride1 = TaxiRide(2)
    ride2 = TaxiRide(2.5)

    ride1.calculate_fare(12)
    ride2.calculate_fare(7.4)

    ride1.print_receipt()
    ride2.print_receipt()

if __name__ == "__main__":
    main()