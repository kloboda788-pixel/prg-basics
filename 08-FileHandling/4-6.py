###
# Counts lines, characters and words in a text file
#

# Returns the number of lines, characters and words in the text
def count_text(text):
    lines = len(text.splitlines())
    characters = len(text)
    words = len(text.split())
    return lines, characters, words

def main():
    file_name = input('File name: ')
    # try - code that may cause an error
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
    # except - what to do when the file does not exist
    except FileNotFoundError:
        print(f'The file {file_name} does not exist.')
    else:
        # else - runs only when there was no error
        lines, characters, words = count_text(content)
        print('Number of lines:', lines)
        print('Number of characters:', characters)
        print('Number of words:', words)

if __name__ == "__main__":
    main()