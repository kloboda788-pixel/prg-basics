# as few coins as possible: 5pln, 2 pln, 1 pln
amount = int(input('Enter the amount in PLN: '))

coins_5 = amount // 5
rest = amount % 5
coins_2 = rest // 2
coins_1 = rest % 2

print(f'The amount of PLN {amount} in coins:')
print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')