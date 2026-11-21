###
# Prints employees employed in a specified position.
#

# Employee List (the file has the .csv extension)
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

number = 1
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        # 'in' checks if the text appears in the line
        if job_title in line:
            print(f'{number}. {line}', end="")
            number += 1