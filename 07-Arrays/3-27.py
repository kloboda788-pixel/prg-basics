import matplotlib.pyplot as plt

x = []
y = []

# create x values from -100 to 100
for n in range(-100, 101):
    x = x + [n]

# create y values: f(x) = x^2 - 3
for n in x:
    y = y + [n ** 2 - 3]

# print chart
plt.plot(x, y)
plt.title('f(x) = x^2 - 3')
plt.show()