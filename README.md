# ALX Backend Python — Programming Paradigms and OOP

## Overview
- This repository contains two cohesive learning tracks:
  - Programming Paradigms & Exception Handling: foundational OOP, error handling, and unit testing
  - More about OOP: advanced OOP topics including magic methods, inheritance, composition, polymorphism, and class vs static methods
- All tasks are implemented with clean, readable code and professional comments for clarity and maintainability.

## Repository Structure
- `programming_paradigm/`
  - `bank_account.py` — `BankAccount` class with `deposit`, `withdraw`, `display_balance`
  - `main-0.py` — CLI for bank operations (deposit/withdraw/display)
  - `robust_division_calculator.py` — `safe_divide` with robust error handling
  - `main.py` — CLI for robust division, later repurposed for library demo
  - `library_management.py` — basic OOP: `Book` and `Library` with availability
  - `simple_calculator.py` — arithmetic operations for unit testing
  - `test_simple_calculator.py` — unit tests using `unittest`
- `oop/`
  - `book_class.py` — `Book` with `__init__`, `__del__`, `__str__`, `__repr__`
  - `library_system.py` — inheritance (`Book`, `EBook`, `PrintBook`) + composition (`Library`)
  - `main.py` — demo for `library_system`
  - `polymorphism_demo.py` — `Shape`, `Rectangle`, `Circle` overriding `area`
  - `class_static_methods_demo.py` — `Calculator` with `@staticmethod add` and `@classmethod multiply`

## Prerequisites
- Python 3.12+
- Windows PowerShell (commands shown use PowerShell syntax)

## Quick Start
- Clone the repo and navigate to the project root.

### Task: BankAccount CLI
- Deposit: `python programming_paradigm/main-0.py deposit:50`
- Withdraw: `python programming_paradigm/main-0.py withdraw:20`
- Display: `python programming_paradigm/main-0.py display`

### Task: Robust Division CLI
- Normal: `python programming_paradigm/main.py 10 5`
- Divide by zero: `python programming_paradigm/main.py 10 0`
- Invalid input: `python programming_paradigm/main.py ten 5`

### Task: Unit Tests
- Run tests: `python -m unittest programming_paradigm/test_simple_calculator.py -v`

### Task: Basic Library Management (Programming Paradigm)
- Demo: `python programming_paradigm/main.py`
- Shows availability changes when checking out and returning books.

### Task: Magic Methods (OOP)
- Usage snippet:
  - `from oop.book_class import Book`
  - `b = Book("1984", "George Orwell", 1949)`
  - `print(b)` → `1984 by George Orwell, published in 1949`
  - `print(repr(b))` → `Book('1984', 'George Orwell', 1949)`
  - `del b` → `Deleting 1984`

### Task: Inheritance + Composition (OOP)
- Demo: `python oop/main.py`
- Prints details for `Book`, `EBook`, and `PrintBook` managed by `Library`.

### Task: Polymorphism (OOP)
- Snippet: `python -c "from oop.polymorphism_demo import Rectangle, Circle; print(f'The area of the Rectangle is: {Rectangle(10,5).area()}'); print(f'The area of the Circle is: {Circle(7).area()}')"`

### Task: Class vs Static Methods (OOP)
- Snippet: `python -c "from oop.class_static_methods_demo import Calculator; print(f'The sum is: {Calculator.add(10,5)}'); res = Calculator.multiply(10,5); print(f'The product is: {res}')"`

## Notes on Design
- Clear separation between demos and core logic for ease of testing.
- Professional docstrings and comments emphasize intent, contracts, and safe practices.
- Outputs match strict checker expectations (e.g., integer vs float formatting).

## Contributing
- Keep code idiomatic and well-documented.
- Prefer adding tests for new features.
