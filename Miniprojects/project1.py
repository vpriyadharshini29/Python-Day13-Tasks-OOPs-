from datetime import datetime, timedelta

# Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

# Member class
class Member:
    def __init__(self, name):
        self.name = name
        self.__borrowed_books = []

    def borrow_book(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        self.__borrowed_books.remove(book)

    def borrowed_books(self):
        return self.__borrowed_books

# Librarian class
class Librarian:
    def __init__(self, name):
        self.name = name

    def add_book(self, library, book):
        library.books.append(book)

    def remove_book(self, library, isbn):
        library.books = [b for b in library.books if b.isbn != isbn]

    def search_book(self, library, title):
        return [book for book in library.books if title.lower() in book.title.lower()]

# Transaction class
class Transaction:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.date = datetime.now()
        self.due_date = self.date + timedelta(days=14)

    def __str__(self):
        return f"{self.member.name} borrowed '{self.book.title}' on {self.date.date()}, due on {self.due_date.date()}"

# Library class
class Library:
    def __init__(self):
        self.books = []
        self.transactions = []

    def borrow_book(self, book, member):
        if book in self.books:
            member.borrow_book(book)
            self.books.remove(book)
            transaction = Transaction(book, member)
            self.transactions.append(transaction)
            print(transaction)
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book, member):
        if book in member.borrowed_books():
            member.return_book(book)
            self.books.append(book)
            print(f"{member.name} returned '{book.title}'.")
        else:
            print(f"{member.name} does not have '{book.title}'.")

    def __len__(self):
        return len(self.books)

# Example Usage
library = Library()
librarian = Librarian("Emma")

book1 = Book("Python Programming", "John Doe", "123")
book2 = Book("Data Structures", "Alice Smith", "456")

librarian.add_book(library, book1)
librarian.add_book(library, book2)

member1 = Member("Mike")

library.borrow_book(book1, member1)
library.return_book(book1, member1)

print("Books in library:", len(library))
