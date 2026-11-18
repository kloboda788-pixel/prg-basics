arr = [7, 9, 2, 4, 5, 6]
print('arr =', arr)

even_numbers = []
odd_numbers = []
# Put every number into one of two lists
for number in arr:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# + joins two lists: even numbers first, then odd numbers
arr = even_numbers + odd_numbers
print('arr =', arr)