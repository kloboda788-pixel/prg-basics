# Returns True if the number is in the range <x, y> (x and y included)
def in_range(number, x, y):
    # Chained comparison: same as x <= number and number <= y
    return x <= number <= y