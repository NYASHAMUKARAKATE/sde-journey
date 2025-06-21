from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, is_available=True, borrow_date=None, due_date=None, return_date=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} ({status})"
    
    def checkout(self, loan_period=14):
        self.borrow_date = datetime.now()
        self.due_date = self.borrow_date + timedelta(days=loan_period)
        self.is_available = False
    
    def return_book(self):
        self.return_date = datetime.now()
        self.is_available = True

    def search_match(self, query):
        return query.lower() in self.title.lower() or query.lower() in self.author.lower() or query.lower() in self.isbn

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "is_available": self.is_available,
            "borrow_date": self.borrow_date.isoformat() if self.borrow_date else None,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "return_date": self.return_date.isoformat() if self.return_date else None
        }

    @classmethod
    def from_dict(cls, data):
        def parse_date(val):
            return datetime.fromisoformat(val) if val else None
        return cls(
            data["title"],
            data["author"],
            data["isbn"],
            data.get("is_available", True),
            parse_date(data.get("borrow_date")),
            parse_date(data.get("due_date")),
            parse_date(data.get("return_date"))
        )

