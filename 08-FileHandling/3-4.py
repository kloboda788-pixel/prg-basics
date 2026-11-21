###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
# encoding='utf-8' - the file contains the € sign
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# regular expression pattern for amounts:
# the € sign followed by one or more digits;
# the brackets ( ) mean that only the digits are returned
pattern = r'€(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)
print('Amounts found:', amounts)

# calculate the total purchases
total = 0
for amount in amounts:
    # findall() returns texts, so they are changed into numbers
    total += int(amount)

# print result
print(f'Total money spent: €{total}')