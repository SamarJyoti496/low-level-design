from .enums import BookStatus

class Book:
    """Represents the abstract book information (metadata)."""
    def __init__(self, isbn: str, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author

class BookItem:
    """Represents a specific physical copy of a book."""
    def __init__(self, book: Book, barcode: str):
        self.book = book  # Association with the abstract Book
        self.barcode = barcode
        self.status = BookStatus.AVAILABLE