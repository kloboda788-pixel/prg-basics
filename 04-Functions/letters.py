# Returns how many times the letter appears in the text
def count_letter(text, letter):
    counter = 0
    # Check every character of the text one by one
    for char in text:
        if char == letter:
            counter += 1
    return counter