import random

arr1 = [3, 7, 1, 0, 4]
# A list of lists (2D array): 3 rows, 2 columns
arr2 = [[2, 3], [7, 1], [0, 4]]
arr2.append([0, 5, 6])


# List comprehension: [value for i in range(...)] creates a list in one line
# Five times the value 7
arr3 = [7 for i in range(5)]
# Numbers from 1 to 9
arr4 = [i for i in range(1, 10)]
# Numbers from 1 to 9 multiplied by 2
arr5 = [i * 2 for i in range(1, 10)]
# 10 random numbers from 1 to 20
arr6 = [random.randint(1, 20) for i in range(10)]
# 5 empty lists
arr7 = [[] for i in range(5)]
# 4 rows, each row has 2 values of 1
arr8 = [[1 for i in range(2)] for j in range(4)]
# 5 rows, each row has 3 random numbers
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]

# Arrays described in the task
arr10 = [4, 0, 3]
# 15 zeros
arr11 = [0 for i in range(15)]
# Numbers from 1 to 30 (31 is not included)
arr12 = [i for i in range(1, 31)]
# 20 random values: 0 or 1
arr13 = [random.randint(0, 1) for i in range(20)]
# 5 rows, 2 columns filled with False
arr14 = [[False for i in range(2)] for j in range(5)]

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)
print(arr10)
print(arr11)
print(arr12)
print(arr13)
print(arr14)