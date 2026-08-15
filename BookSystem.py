
available_books = [
    "Python",
    "Data Structures",
    "Machine Learning",
    "Database",
    "Operating Systems"
]
borrowed_books = []

def show_books():
    if len(available_books) == 0:
        print("no books available")
    else:
        print("available books: ")
        for i, book in enumerate(available_books):
            print(i+1, book)

def borrow_book():
    show_books()

    if len(available_books) == 0:
        return
    book = input("Enter the name of the book to borrow: ")
    if book in available_books:
        available_books.remove(book)
        borrowed_books.append(book)
        print(book, "has been borrowed successfully")
    else:
        print("Book is unavailable.")

def return_book():
    if len(borrowed_books) == 0:
        print("You have not borrowed any books.")
        return

    print("Borrowed Books:")
    for book in borrowed_books:
        print(book)

    book = input("Enter the name of the book to return: ")

    if book in borrowed_books:
        borrowed_books.remove(book)
        available_books.append(book)
        print(book, "has been returned successfully")
    else:
        print("You did not borrow this book.")

def show_borrowed_books():
    if len(borrowed_books) == 0:
        print("No books are borrowed")
    else:
        print("borrowed books:")
        for book in borrowed_books:
            print(book)

