# sprawdzanie czy 1 lub 6

import random
dice_roll = random.randint(1,6)
is_one_or_six = dice_roll == 1 or dice_roll == 6
print(f'Roll: {dice_roll}, Is 1 or 6: {is_one_or_six}')
