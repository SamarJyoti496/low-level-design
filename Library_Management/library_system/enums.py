from enum import Enum, auto

class BookStatus(Enum):
     AVAILABLE=auto()
     LOANED=auto()
     RESERVED=auto()
     LOST=auto()
