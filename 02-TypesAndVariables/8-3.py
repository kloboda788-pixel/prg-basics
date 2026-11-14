###
# A program that reads temperature in degrees Celsius from the keyboard.
# Then it calculates and prints the temperature in Kelvin and Fahrenheit.
#

# read temperature in degrees Celsius from the keyboard
celsius = float(input('Enter temperature in degrees Celsius: '))

# convert to Kelvin: K = C + 273.15
kelvin = celsius + 273.15

# convert to Fahrenheit: F = C * 9/5 + 32
fahrenheit = celsius * 9 / 5 + 32

# print results
print(f'{celsius:.2f} C = {kelvin:.2f} K = {fahrenheit:.2f} F')