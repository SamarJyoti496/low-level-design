from .users import Member
from .catalog import Book, BookItem
from .enums import BookStatus

class Library:
    """The main library class managing books and members."""
    def __init__(self, name: str):
        self.name = name
        # Aggregation: The Library holds lists of objects, but doesn't own them.
        self.book_items = []
        self.members = []
        print(f"Library '{self.name}' is now open.")

    def add_member(self, user_id, name):
        member = Member(user_id, name)
        self.members.append(member)
        return member

    def add_book_item(self, book: Book, barcode: str):
        book_item = BookItem(book, barcode)
        self.book_items.append(book_item)
        print(f"Added '{book.title}' (Barcode: {barcode}) to the library.")

    def issue_book(self, member: Member, barcode: str):
        book_item = self._find_book_item(barcode)

        if book_item and book_item.status == BookStatus.AVAILABLE:
            book_item.status = BookStatus.LOANED
            member.borrow_book(book_item)
            return True
        elif not book_item:
            print(f"ERROR: Book with barcode {barcode} not found.")
        else:
            print(f"ERROR: '{book_item.book.title}' is currently unavailable.")
        return False

    def return_book(self, member: Member, barcode: str):
        book_item = self._find_book_item(barcode)
        if book_item and book_item in member.card.borrowed_books:
            book_item.status = BookStatus.AVAILABLE
            member.return_book(book_item)
            return True
        print("ERROR: Book return failed.")
        return False

    def _find_book_item(self, barcode: str) -> BookItem | None:
        for item in self.book_items:
            if item.barcode == barcode:
               return item
        return None