# Obliczanie odległosci do horyzontu
import math
h = float(input("Enter the height in meters: "))
d = 3.57 * math.sqrt(h)
print("The distance to the horizon is:", round(d, 2), "km")
# Plaza 1.78 m - > 4.76 km
# Hotel 20 m - > 15.96 km