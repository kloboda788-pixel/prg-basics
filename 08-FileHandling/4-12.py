###
# Copies books of a given genre to separate files
#
import csv

# pairs (tuples): genre, file name
GENRE_FILES = [
    ('Fantasy', 'books_fantasy.txt'),
    ('Historical', 'books_historical.txt'),
    ('Romance', 'books_romance.txt'),
    ('Classic', 'books_classic.txt')
]

# Returns all books from the CSV file as a list of rows (lists)
def read_books(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # next() skips the header line
        next(reader)
        return list(reader)

# Returns only the books of the given genre
def books_by_genre(books, genre):
    result = []
    for book in books:
        # row: [Title, Author, Genre, Year] - column 2 is the genre
        if book[2] == genre:
            result.append(book)
    return result

# Saves the books to a file, one book per line
def save_books(books, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for book in books:
            # join() glues the list back into one line with commas
            file.write(','.join(book) + '\n')

def main():
    books = read_books('books.csv')
    # every pair is unpacked into two variables: genre and file_name
    for genre, file_name in GENRE_FILES:
        selected = books_by_genre(books, genre)
        save_books(selected, file_name)
        print(f'{genre}: {len(selected)} books saved to {file_name}')

if __name__ == "__main__":
    main()