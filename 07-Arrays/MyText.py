# Module with functions operating on a text

# Returns the number of words in the text
def word_count(text):
    # split() divides the text into a list of words
    return len(text.split())

# Returns words ordered from the longest to the shortest
def words_by_length(text):
    # key=len - sort by word length, reverse=True - from the longest
    return sorted(text.split(), key=len, reverse=True)

# Returns words ordered alphabetically
def words_alphabetically(text):
    # key=str.lower - ignore letter case, so "An" is next to "a"
    return sorted(text.split(), key=str.lower)