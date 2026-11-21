import queue

###
# Calculates RPN (Reverse Polish Notation) expressions using a stack
#
stack = queue.LifoQueue()

print('Enter numbers, operators (+ - * /) or = to get the result.')
while True:
    value = input('> ').strip()

    if value in ['+', '-', '*', '/']:
        # pop two numbers; the one on top is the SECOND operand
        b = stack.get()
        a = stack.get()
        if value == '+':
            result = a + b
        elif value == '-':
            result = a - b
        elif value == '*':
            result = a * b
        else:
            result = a / b
        # push the result back on the stack
        stack.put(result)

    elif value == '=':
        # the final result is the only element left on the stack
        print('Result:', stack.get())
        break

    else:
        # any other value is a number - push it on the stack
        stack.put(float(value))