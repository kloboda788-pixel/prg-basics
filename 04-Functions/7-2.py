def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Main program logic is kept in one function
def main():
    x = 10
    y = 5
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")

# Runs main() only when this file is started directly,
# not when it is imported as a module
if __name__ == "__main__":
    main()