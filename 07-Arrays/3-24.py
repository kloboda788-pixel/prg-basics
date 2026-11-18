import random

# Returns a randomly selected element of the array
def rand_elem(array):
    # Random index from 0 to the last index
    index = random.randint(0, len(array) - 1)
    return array[index]

def main():
    colors = ['red', 'green', 'blue', 'yellow', 'black']
    print('Array:', colors)
    for i in range(5):
        print('Random element:', rand_elem(colors))

if __name__ == "__main__":
    main()