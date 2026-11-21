###
# Calculates the total cost of a shopping cart
#

# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
total = 0
for product, quantity in cart.items():
    # the same key (product name) is used to find its price in the price list
    cost = prices[product] * quantity
    print(f'{product}: {quantity} x {prices[product]:.2f} = {cost:.2f}')
    total += cost

print(f'Total cost: {total:.2f}')