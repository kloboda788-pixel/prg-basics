###
# Module with a class describing an e-book
#
class EBook:
    # initial values are given when the object is created
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False     # a new book is closed

    def open(self):
        self.is_open = True
        print(f'"{self.title}" is open.')

    def close(self):
        self.is_open = False
        print(f'"{self.title}" is closed.')

    # Goes to the next page - only when the book is open and not on the last page
    def next_page(self):
        if not self.is_open:
            print('The book is closed - open it first.')
        elif self.current_page < self.pages:
            self.current_page += 1
        else:
            print('This is the last page.')

    # Goes to the previous page - only when the book is open and not on page 1
    def previous_page(self):
        if not self.is_open:
            print('The book is closed - open it first.')
        elif self.current_page > 1:
            self.current_page -= 1
        else:
            print('This is the first page.')

    # Prints title, author, number of pages and the current page
    def show_status(self):
        state = 'open' if self.is_open else 'closed'
        print(f'{self.title} by {self.author}, {self.pages} pages, '
              f'current page: {self.current_page} ({state})')