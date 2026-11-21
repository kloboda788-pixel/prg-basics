import queue

###
# Operations on a stack (LIFO - Last In, First Out)
#

# creates a stack
numbers = queue.LifoQueue()

# put() adds an element to the top of the stack
for number in [2, 3, 7, 4, 1, 9, 8]:
    numbers.put(number)

# get() takes the element from the top - the last one added
last = numbers.get()          # 8
second_last = numbers.get()   # 9
print('Sum of the last two numbers:', last + second_last)

# sum the remaining elements; empty() is True when the stack has no elements
total = 0
while not numbers.empty():
    total += numbers.get()
print('Sum of the remaining numbers:', total)