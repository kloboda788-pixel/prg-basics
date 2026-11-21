import json

###
# Displays Euro exchange rates saved from the NBP API
#
with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# :<16 - every column is 16 characters wide, aligned to the left
print(f'{"Date":<16}{"Buying Rate":<16}{"Selling Rate"}')
print('=' * 44)

# "rates" is a list of dictionaries; bid = buying rate, ask = selling rate
for rate in data['rates']:
    print(f"{rate['effectiveDate']:<16}{rate['bid']:<16.4f}{rate['ask']:.4f}")