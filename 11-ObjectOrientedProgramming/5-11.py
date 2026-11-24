###
# Class describing a stadium with sectors
#
class C:
    # sectors - a dictionary: sector letter -> number of fans
    def __init__(self, sectors):
        self.sectors = sectors

    # Changes the number of fans in sector s or adds a new sector s
    def m1(self, s, n):
        # assigning to a key changes the value or adds a new pair
        self.sectors[s] = n

    # Returns the sum of fans in the sectors listed in the string s
    def m2(self, s):
        total = 0
        for letter in s:
            # get(letter, 0) - a sector that does not exist counts as 0
            total += self.sectors.get(letter, 0)
        return total

if __name__ == "__main__":
    c = C({"A": 120, "D": 150, "G": 90, "K": 110})
    c.m1("G", 130)
    print(c.m2("GD"))     # 280
    print(c.m2("KEJ"))    # 110