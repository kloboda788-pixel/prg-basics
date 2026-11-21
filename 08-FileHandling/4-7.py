###
# Counts vowels in a text entered from the keyboard
#
import re

text = input('Enter text: ')

# [aeiou] - any one of these letters
# re.IGNORECASE - small and capital letters are treated the same
vowels = re.findall(r'[aeiou]', text, re.IGNORECASE)

print('Number of vowels:', len(vowels))