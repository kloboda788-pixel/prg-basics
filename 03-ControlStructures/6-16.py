# Calculates and prints the total washing time.

total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').lower()
extra_rinse = input('Extra rinse? (y/n): ').lower()
extra_spin = input('Extra spin? (y/n): ').lower()
program_ok = True

if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20
else:
    program_ok = False
    print('Invalid washing program')

if program_ok:
    if extra_rinse == 'y':
        total_washing_time += 15
    if extra_spin == 'y':
        total_washing_time += 9
    print(f'Total washing time: {total_washing_time} minutes')