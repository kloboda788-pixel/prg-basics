# Masks the 16-digit card number:
# first 2 digits + 10 asterisks + last 4 digits
def hide(card_number):
    # [:2] - first two characters, [-4:] - last four characters
    return card_number[:2] + '*' * 10 + card_number[-4:]