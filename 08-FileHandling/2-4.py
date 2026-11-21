###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
# the first file is opened for reading, the second one for writing
with open(employees_file, 'r', encoding='utf-8') as source:
    with open(position_file, 'w', encoding='utf-8') as target:
        for line in source:
            if job_title in line:
                # the line already ends with \n, so it is written as it is
                target.write(line)

print(f'Employees have been saved to {position_file}.')