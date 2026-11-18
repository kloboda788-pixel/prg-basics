array = [2, 3, 2, 5, 8, 1, 9, 8]

print('Array:', end=' ')
for element in array:
    print(element, end=' ')
print()

print('Unique elements:', end=' ')
for element in array:
    # A unique element appears in the array exactly once
    if array.count(element) == 1:
        print(element, end=' ')
print()