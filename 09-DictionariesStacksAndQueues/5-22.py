import json

###
# Reads product data from the keyboard and saves it to a JSON file
#
product = {}

# read product data from keyboard
product['name'] = input('Product name: ')
# float() changes the text into a real number, round() keeps two decimal places
product['price'] = round(float(input('Price: ')), 2)
# the comparison gives True or False, so the value is a bool
product['paid'] = input('Paid (yes/no): ').strip().lower() == 'yes'

# save product data to json file
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print('Saved:', product)