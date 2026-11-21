###
# Prints Graphic Designers from a CSV file using the csv module
#
import csv

file_name = 'it_company.csv'
job_title = 'Graphic Designer'

print('GRAPHIC DESIGNERS')
print('=================')

with open(file_name, 'r', encoding='utf-8') as file:
    # csv.reader splits every line at commas into a list:
    # [Last Name, First Name, Job Title, Email]
    reader = csv.reader(file)
    # next() skips the header line
    next(reader)
    for row in reader:
        if row[2] == job_title:
            # first name, last name, email - in this order
            print(f'{row[1]} {row[0]},{row[3]}')