###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
# encoding='utf-8' - the file contains special characters (e.g. ’)
with open(original_file, 'r', encoding='utf-8') as file:
    content = file.read()

# write the content to the target file (copy)
with open(target_file, 'w', encoding='utf-8') as file:
    file.write(content)

print(f'{original_file} has been copied to {target_file}.')