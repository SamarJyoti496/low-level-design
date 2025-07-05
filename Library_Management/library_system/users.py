from abc import ABC, abstractmethod
import datetime

class LibraryCard:
    """Represents a member's library card. Owned by the Member class."""
    def __init__(self, member_id: str):
        self.card_id = f"CARD-{member_id}"
        self.issue_date = datetime.date.today()
        self.borrowed_books = []

    def add_borrowed_book(self, book_item):
        self.borrowed_books.append(book_item)

    def remove_borrowed_book(self, book_item):
        self.borrowed_books.remove(book_item)

class User(ABC):
    """Abstract base class for all users."""
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name

    @abstractmethod
    def get_details(self) -> str:
        pass

class Member(User):
    """A concrete user who can borrow and return books."""
    def __init__(self, user_id: str, name: str):
        super().__init__(user_id, name)
        # Composition: The Member object creates and owns its LibraryCard.
        self.card = LibraryCard(self.user_id)
        print(f"Member '{self.name}' created with Card ID: {self.card.card_id}")

    def get_details(self) -> str:
        return f"Member: {self.name} (ID: {self.user_id})"

    def borrow_book(self, book_item):
        self.card.add_borrowed_book(book_item)
        print(f"'{self.name}' borrowed '{book_item.book.title}'.")

    def return_book(self, book_item):
        self.card.remove_borrowed_book(book_item)
        print(f"'{self.name}' returned '{book_item.book.title}'.")

class Librarian(User):
    """A concrete user who manages the library."""
    def get_details(self) -> str:
        return f"Librarian: {self.name} (ID: {self.user_id})"

    def add_book_item(self, library, book, barcode):
        library.add_book_item(book, barcode)

    def add_member(self, library, user_id, name):
        return library.add_member(user_id, name)

