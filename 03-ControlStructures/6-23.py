# multiplication table for numbers <1,10>
number = int(input('Enter number: '))
for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')