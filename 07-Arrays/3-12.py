array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

print('Numbers from the first array that are not in the second array:')
for number in array1:
    # 'not in' checks if the value does not appear in the list
    if number not in array2:
        print(number, end=' ')
print()