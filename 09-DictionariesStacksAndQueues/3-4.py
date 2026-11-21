import queue

###
# Converts a natural number to a binary number using a stack
#
def to_binary(number):
    # zero is a special case: the loop below would not run at all
    if number == 0:
        return '0'
    stack = queue.LifoQueue()
    while number > 0:
        # put the remainder of dividing by 2 on the stack
        stack.put(number % 2)
        number = number // 2
    # the remainders are read in reverse order - exactly what a stack does
    binary = ''
    while not stack.empty():
        binary += str(stack.get())
    return binary

number = int(input('Natural number: '))
print('Binary number:', to_binary(number))