import MyText

def main():
    text = 'An apple a day keeps the doctor away'
    print('Text:', text)
    print('Number of words:', MyText.word_count(text))
    # ','.join(list) joins the list elements with commas
    print('Words from the longest:', ','.join(MyText.words_by_length(text)))
    print('Words ordered alphabetically:', ','.join(MyText.words_alphabetically(text)))

if __name__ == "__main__":
    main()