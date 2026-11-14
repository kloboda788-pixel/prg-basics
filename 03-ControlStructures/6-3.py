###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = input('Is switch 1 on? (y/n): ').lower() == 'y'
light_switch2 = input('Is switch 2 on? (y/n): ').lower() == 'y'
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
print(f'Number of bulbs on: {bulbs_on}')