###
# Calculation of circle area and circumference
#

# determine radius and PI values
r = float(input('Enter radius: '))
pi = 3.14

# calculate area
area = pi * r ** 2

# calculate circumference
circumference = 2 * pi * r

# print results
print(f'Circumference = {circumference:.2f}, area = {area:.2f}')

# r = 1 --> circumference = 6.28, area = 3.14
# r = 3 --> circumference = 18.84, area = 28.26