# PIN check, three attempts
pin = '0805'
attempts = 0
pin_ok = False

while attempts < 3 and not pin_ok:
    entered_pin = input('Enter the PIN code: ')
    attempts += 1
    if entered_pin == pin:
        pin_ok = True
        print('PIN correct. Payment accepted.')
    else:
        print('Incorrect...')

if not pin_ok:
    print('Sorry, your payment card has been blocked.')