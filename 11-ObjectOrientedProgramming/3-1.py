###
# __str__ - the text representation of an object
#
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # __str__ is called automatically by print() and str()
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2021)

# Print the object
print(my_car)  # Output: 2021 Toyota Corolla