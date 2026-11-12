 # liczba dodatnie czy ujemna
input_number = float(input('Enter a number: '))
if input_number > 0:
    print(f'{input_number} is positive')
elif input_number < 0:
    print(f'{input_number} is negative')
else:
    print(f'{input_number} is zero')