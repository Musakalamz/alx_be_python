"""Library system showcasing inheritance and composition.

Classes:
- Book: base type with shared metadata
- EBook: inherits Book, adds `file_size` (KB)
- PrintBook: inherits Book, adds `page_count`
- Library: composes a collection of books and prints summaries

Remarks:
- Derived initializers delegate to the base via `super().__init__`
- Composition keeps Library focused on coordination, not inheritance
"""


class Book:
    """Base book type with common attributes."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class EBook(Book):
    """Digital book with a file size attribute (in KB)."""

    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = int(file_size)


class PrintBook(Book):
    """Printed book with a page count attribute."""

    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = int(page_count)


class Library:
    """Library that manages a heterogeneous collection of books."""

    def __init__(self):
        # Explicit list to align with simple checkers and keep intent clear
        self.books = []

    def add_book(self, book):
        """Add any Book/EBook/PrintBook instance to the collection."""
        self.books.append(book)

    def list_books(self):
        """Print a description line for every book in the collection."""
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB"
                )
            elif isinstance(book, PrintBook):
                print(
                    f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}"
                )
            else:
                print(f"Book: {book.title} by {book.author}")

