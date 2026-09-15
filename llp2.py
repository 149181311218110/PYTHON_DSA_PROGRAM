class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered")


class Book:
    def __init__(self, title):
        self.title = title


class Member:
    def __init__(self, name):
        self.name = name


library = Library()
book1 = Book("Python Programming")
member1 = Member("Arun")

library.add_book(book1)
library.register_member(member1)