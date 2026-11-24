###
# Class with a list of points on the plane
#
class C:
    # points - a 2D array: [[x, y], [x, y], ...]
    def __init__(self, points):
        self.points = points

    # Returns True if at least n points are in the first quadrant (x > 0 and y > 0)
    def m(self, n):
        counter = 0
        for x, y in self.points:
            if x > 0 and y > 0:
                counter += 1
        return counter >= n

if __name__ == "__main__":
    c = C([[2, 3], [1, 8], [-6, 4], [3, -7]])
    print(c.m(2))    # True
    print(c.m(3))    # False