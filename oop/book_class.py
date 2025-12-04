"""Book class demonstrating core Python magic methods.

This module showcases idiomatic use of:
- Constructor (`__init__`) for robust attribute initialization
- Destructor (`__del__`) for lifecycle visibility in small scripts
- String representations (`__str__` and `__repr__`) with clear contracts

Design notes from long-term production experience:
- `__str__` is for user-facing readability; keep it concise and stable
- `__repr__` should aim to be unambiguous and, when feasible, evaluable
- `__del__` is best-effort only; avoid side effects beyond diagnostics
"""

from typing import Any


class Book:
    """A simple immutable-ish record of book metadata.

    Attributes:
        title: Human-readable title of the work
        author: Primary author attribution
        year: Publication year (Gregorian)
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        """Initialize a Book with validated basic types.

        Defensive checks are intentionally lightweight; real systems might
        normalize Unicode, validate ranges, and enforce domain constraints.
        """
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __del__(self):  # pragma: no cover
        """Destructor prints a simple lifecycle message.

        In CPython, objects are reference-counted, and `__del__` generally
        runs promptly when the refcount hits zero. In other interpreters or
        complex cycles, it may be deferred or skipped at process exit.
        """
        try:
            print(f"Deleting {self.title}")
        except Exception:
            # Avoid raising during interpreter shutdown
            pass

    def __str__(self):
        """Human-friendly description used by `print()` and f-strings."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that can recreate the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

