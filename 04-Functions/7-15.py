# Returns True if at least 3 people were in the room at the same time
def f(detector):
    # Number of people currently in the room
    people = 0
    for sign in detector:
        if sign == '+':
            people += 1
        elif sign == '-':
            people -= 1
        # Check after every change - no need to look further
        if people >= 3:
            return True
    return False

if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))