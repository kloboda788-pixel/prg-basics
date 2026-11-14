###
# A program that prints your height both in cm and in feet and inches.
# 1 inch = 2.54 cm, 1 foot = 12 inches
#
cm = 178

# convert height to inches (rounded to whole inches)
total_inches = round(cm / 2.54)

# calculate the number of feet (division without remainder)
feet = total_inches // 12

# the remaining inches (remainder of the division)
inches = total_inches % 12

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')