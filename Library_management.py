# Define the Book class
class Book:
    def __init__(self, title, author, published_year, available):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.available = available

# Define the Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}, published in {book.published_year}, available: {book.available}")

# Create a new library
my_library = Library()

# Add some books to the library
my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, True))
my_library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960, True))
my_library.add_book(Book("1984", "George Orwell", 1949, False))

# Search for a book
book = my_library.search_book("The Great Gatsby")
if book:
    print(f"Found {book.title} by {book.author}")
else:
    print("Book not found")

# Display all books
my_library.display_books()
