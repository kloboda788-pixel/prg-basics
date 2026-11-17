###
# Draw a square
#
def draw_square(pen, length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    for i in range(3):
        pen.forward(length)
        pen.right(120)

def draw_rectangle(pen, width, height):
    for i in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)