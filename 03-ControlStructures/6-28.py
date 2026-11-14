# ciag Fibonacciego
a = 0
b = 1
for i in range(20):
    print(a, end=' ')
    next_term = a + b
    a = b
    b = next_term
print()