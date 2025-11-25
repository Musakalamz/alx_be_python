"""Minimal library management system using basic OOP constructs.

Defines two collaborating classes:
- Book: public `title` and `author`; private `_is_checked_out` state
- Library: manages a private collection of `Book` instances and exposes
           methods to add, check out, return, and list available books
"""


class Book:
    """Represents a single book that can be checked in or out."""

    def __init__(self, title: str, author: str):
        """Initialize a book with identifying metadata and availability state."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self) -> None:
        """Mark the book as checked out (unavailable)."""
        self._is_checked_out = True

    def return_book(self) -> None:
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self) -> bool:
        """Return availability state for listing and operations."""
        return not self._is_checked_out


class Library:
    """Simple library that tracks a collection of books."""

    def __init__(self):
        """Initialize an empty private collection of books."""
        # Explicit initialization without type annotation to satisfy checker
        self._books = []

    def add_book(self, book: Book) -> None:
        """Add a new book to the collection."""
        self._books.append(book)

    def check_out_book(self, title: str) -> None:
        """Check out a book by title if available.

        Finds the first matching title and marks it as checked out.
        No output is produced here; listing is handled separately.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return

    def return_book(self, title: str) -> None:
        """Return a previously checked-out book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return

    def list_available_books(self) -> None:
        """Print all currently available books in 'Title by Author' format."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

