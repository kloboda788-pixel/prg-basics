###
# Counts how many times each word appears in a paragraph
#
paragraph = "cat dog mouse cat rat cat mouse"

# key = word, value = how many times it appears
word_count = {}

for word in paragraph.split():
    if word in word_count:
        # the word is already in the dictionary - increase its counter
        word_count[word] += 1
    else:
        # a new word - add it with the counter 1
        word_count[word] = 1

for word, count in word_count.items():
    print(f'{word}: {count}')