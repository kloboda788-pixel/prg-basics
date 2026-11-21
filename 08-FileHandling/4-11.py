###
# Prints and saves numbers from 1 to 100 with their 2nd and 3rd powers
#
file_name = 'powers.txt'

with open(file_name, 'w', encoding='utf-8') as file:
    for n in range(1, 101):
        line = f'{n},{n ** 2},{n ** 3}'
        print(line)
        file.write(line + '\n')

print(f'Results saved to {file_name}.')