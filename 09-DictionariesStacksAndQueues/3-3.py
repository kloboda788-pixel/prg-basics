import queue

###
# Checks if brackets in an expression are used correctly
#
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

# Returns True if brackets in expression are ok or False otherwise
def brackets_ok(expression):
    stack = queue.LifoQueue()
    # for every closing bracket - the matching opening bracket
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            # opening bracket - put it on the stack
            stack.put(char)
        elif char in ')]}':
            # closing bracket with nothing to close
            if stack.empty():
                return False
            # the last opened bracket must match this closing bracket
            if stack.get() != pairs[char]:
                return False
        # all other characters are skipped

    # every opened bracket must be closed, so the stack must be empty
    return stack.empty()

for expression in [expression1, expression2, expression3]:
    if brackets_ok(expression):
        print(f'{expression} - brackets ok')
    else:
        print(f'{expression} - brackets not correct')