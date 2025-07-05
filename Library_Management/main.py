# main.py
from library_system.library import Library
from library_system.catalog import Book
from library_system.users import Librarian

def main():
     central_library = Library("Central City Library")

     book1_meta = Book("978-0321765723", "The C++ Programming Language", "Bjarne Stroustrup")
     book2_meta = Book("978-0132350884", "Clean Code", "Robert C. Martin")
     
     librarian = Librarian("L001", "Mr. Smith")
     
     
     librarian.add_book_item(central_library, book1_meta, "CPP001")
     librarian.add_book_item(central_library, book2_meta, "CC001")
     librarian.add_book_item(central_library, book2_meta, "CC002")

     member1 = librarian.add_member(central_library, "M001", "Alice")
     member2 = librarian.add_member(central_library, "M002", "Bob")

     central_library.issue_book(member1, "CC001")

     central_library.issue_book(member2, "CC001")

     central_library.issue_book(member2, "CC002")

     central_library.return_book(member1, "CC001")

     central_library.issue_book(member2, "CC001")


if __name__ == "__main__":
    main()