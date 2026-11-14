# decimal to binary
number = int(input('Enter decimal number: '))
quotient = number
binary = ''

if number == 0:
    binary = '0'

while quotient > 0:
    remainder = quotient % 2
    binary = str(remainder) + binary   # add remainder at the front
    quotient = quotient // 2

print(f'{number}(10) = {binary}(2)')