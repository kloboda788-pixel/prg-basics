###
# Main program using the EBook class
#
import ebook

def main():
    # 1. Create a book - the values go to the __init__ method
    book = ebook.EBook('The Little Prince', 'Antoine de Saint-Exupery', 96)
    # 2. Open a book
    book.open()
    # 3. Display a book status
    book.show_status()
    # 4. Read a few pages
    for i in range(5):
        book.next_page()
    # 5. Display a book status
    book.show_status()
    # 6. Close a book
    book.close()
    # 7. Read a few pages - not possible, the book is closed
    book.next_page()
    book.next_page()
    book.show_status()

if __name__ == "__main__":
    main()