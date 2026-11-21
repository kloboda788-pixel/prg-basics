import queue

###
# Reverses a text using a stack
#
def reverse_text(text):
    stack = queue.LifoQueue()
    # push every character onto the stack
    for char in text:
        stack.put(char)
    # pop the characters - the last one comes out first
    reversed_text = ''
    while not stack.empty():
        reversed_text += stack.get()
    return reversed_text

text = input('Enter text: ')
print('Reversed text:', reverse_text(text))