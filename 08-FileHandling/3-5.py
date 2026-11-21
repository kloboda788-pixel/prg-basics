###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Username: ')
password = input('Password: ')

# pattern (criteria) for username and password
# ^ - start of text, $ - end of text
# [a-z]{6,} - at least 6 lowercase letters
username_pattern = r'^[a-z]{6,}$'
# [A-Za-z0-9_]{8,} - at least 8 letters, digits or underscores
password_pattern = r'^[A-Za-z0-9_]{8,}$'

# check if username and password are ok
# re.match() returns a match object, or None when the text does not match
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match:
    print('Username and password are correct.')
else:
    if not username_match:
        print('Incorrect username: at least 6 characters, only lowercase letters.')
    if not password_match:
        print('Incorrect password: at least 8 characters, only letters, digits and _.')