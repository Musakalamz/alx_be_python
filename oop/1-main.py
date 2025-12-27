
3885




Back-End Web Development
Average: 105.09%
More about OOP
 Weight: 1
 Project over - took place from Dec 1, 2025 12:00 AM to Dec 8, 2025 12:00 AM
In a nutshell…
28.0/28 mandatory
Final score:  100.0%


This project dives deeper into the world of Object-Oriented Programming (OOP) in Python.

You’ll explore advanced concepts like constructors, destructors, magic methods, inheritance, composition, polymorphism, and more.

Project Objectives:
By the end of this project, you should be able to:

Describe the functionalities of constructors (__init__), destructors (__del__), and common magic methods (e.g., __str__, __repr__) in Python classes.
Implement inheritance to create new classes that inherit properties and methods from existing classes.
Utilize composition as an alternative to inheritance for building complex objects.
Explain the concepts of single, multiple, and multilevel inheritance in Python.
Understand the method resolution order (MRO) in Python and how it affects method calls in inheritance hierarchies.
Implement polymorphism and method overriding to create flexible and reusable code.
Explain and use Python’s duck typing to achieve polymorphic behavior.
Distinguish between class methods and static methods based on their usage and purpose.
Apply @classmethod and @staticmethod decorators appropriately in your Python classes.
This project will equip you with a comprehensive understanding of advanced OOP concepts in Python, enabling you to design and build robust and maintainable object-oriented applications.

Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Dive into Python Magic Methods
mandatory
Score: 100.0% (Checks completed: 100.0%)
Objective: Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).

Task Description:
Create a Python script named book_class.py. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

Requirements for Book Class in book_class.py:
Attributes:

title (str): The title of the book.
author (str): The author of the book.
year (int): The publication year of the book.
Magic Methods:

Constructor (__init__): Initializes a Book instance with title, author, and year.
Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)".
Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".
Provided for Testing: main.py
To test your Book class, use the following main.py script, which demonstrates creating a Book instance and utilizing the implemented magic methods:

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
Expected Output:
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984
Repo:

GitHub repository: alx_be_python
Directory: oop
File: book_class.py
  
1. Mastering Inheritance and Composition in Python
mandatory
Score: 100.0% (Checks completed: 100.0%)
Objective: Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.

Task Description:
Develop two Python scripts: library_system.py and main.py. In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. Additionally, implement a Library class demonstrating composition by managing a collection of books.

library_system.py:
Base Class - Book:

Attributes: title (str) and author (str).
Method: __init__(self, title, author) for initializing book attributes.
Derived Classes - EBook and PrintBook:

Both classes inherit from Book.
EBook additional attribute: file_size (int).
PrintBook additional attribute: page_count (int).
Each derived class should have its own __init__ method that properly calls the base class __init__ while also initializing its unique attribute.
Composition - Library:

Attributes: books (a list to store instances of Book, EBook, and PrintBook).
Methods:
add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
list_books(self): Prints details of each book in the library.
main.py (Provided for Testing):
This script tests the functionality of your classes in library_system.py by adding different types of books to a Library instance and listing them.

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()