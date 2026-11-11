# VAT calculation
amount_string = input('Enter amount: ')
amount = float(amount_string)
vat_rate = 0.23
vat_amount = amount * vat_rate
print(f'Amount: {amount:.2f}')
print(f'VAT 23%: {vat_amount:.2f}')