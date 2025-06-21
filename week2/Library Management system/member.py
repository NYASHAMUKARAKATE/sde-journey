class Member:
    def __init__(self, name, member_id, email, borrowed_books=None, fees=0.0):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
        self.fees = fees

    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book.isbn)
            book.is_available = False
            return True
        return False

    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            self.borrowed_books.remove(book.isbn)
            book.is_available = True
            return True
        return False

    def search_match(self, query):
        return query.lower() in self.name.lower() or query.lower() in self.email.lower()

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "email": self.email,
            "borrowed_books": self.borrowed_books,
            "fees": self.fees
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["member_id"],
            data["email"],
            data.get("borrowed_books", []),
            data.get("fees", 0.0)
        )