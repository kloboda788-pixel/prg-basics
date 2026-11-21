###
# Applies a 10% discount to a price list
#
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# Prints products with prices and returns their total value
def print_prices(prices):
    total = 0
    for product, price in prices.items():
        print(f'{product}: {price:.2f}')
        total += price
    return total

print('PRICES BEFORE DISCOUNT')
total_before = print_prices(price_list)
print(f'Total value: {total_before:.2f}')
print()

# Modify the prices - a new value is assigned to every existing key
for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

print('PRICES AFTER 10% DISCOUNT')
total_after = print_prices(price_list)
print(f'Total value: {total_after:.2f}')