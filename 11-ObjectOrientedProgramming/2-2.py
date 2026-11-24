###
# Class describing a square
#
class Square:
    # the side length is given when the object is created
    def __init__(self, a):
        self.a = a

    # Returns the area of the square
    def area(self):
        return self.a * self.a

    # Returns the perimeter of the square
    def perimeter(self):
        return 4 * self.a

square1 = Square(4)
square2 = Square(6)

print('Square with side 4:')
print(f'Area is {square1.area()}, Perimeter is {square1.perimeter()}')
print('Square with side 6:')
print(f'Area is {square2.area()}, Perimeter is {square2.perimeter()}')