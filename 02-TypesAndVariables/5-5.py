# obliczanie rabatu
price_string = input('Enter price: ')
price = float(price_string)
discount_string = input('Enter discount: ')
discount = float(discount_string) / 100
print(f'Price: {price:.2f}')
print(f'Discount: {discount * 100:.0f}%')
print(f'Price after discount: {price * (1 - discount):.2f}')
print(f'Discount amount: {price * discount:.2f}')