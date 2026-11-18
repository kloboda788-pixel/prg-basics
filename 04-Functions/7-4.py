# Import the module with the count_letter() function
import letters

def main():
    text = 'You never get a second chance to make a first impression'
    print(text)
    print(f"The number of letter 'e': {letters.count_letter(text, 'e')}")

if __name__ == "__main__":
    main()