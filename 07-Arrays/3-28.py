import math
import matplotlib.pyplot as plt

x = []
y = []

# Angles from 0 to 360 degrees
for angle in range(0, 361):
    x.append(angle)
    # math.sin() needs radians, so degrees are converted first
    y.append(math.sin(math.radians(angle)))

plt.plot(x, y)
plt.title('y = sin(x)')
plt.xlabel('x [degrees]')
plt.ylabel('sin(x)')
plt.show()