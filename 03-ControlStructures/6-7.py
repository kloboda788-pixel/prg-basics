###
# Checks which age group the user belongs to
# Child: under 13, Teen: 13 to 19, Adult: 20 to 64, Senior: 65 or older
#
age = int(input('Enter your age: '))
if age < 0:
    print('Invalid age')
elif age < 13:
    print('Child')
elif age <= 19:
    print('Teen')
elif age <= 64:
    print('Adult')
else:
    print('Senior')