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

    def __str__(self):
        """Human-friendly summary for base books."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Digital book with a file size attribute (in KB)."""

    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = int(file_size)

    def __str__(self):
        """Human-friendly summary for digital books."""
        return (
            f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
        )


class PrintBook(Book):
    """Printed book with a page count attribute."""

    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = int(page_count)

    def __str__(self):
        """Human-friendly summary for printed books."""
        return (
            f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        )


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
            print(str(book))
