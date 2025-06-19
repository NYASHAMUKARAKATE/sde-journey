class Member:
    def __init__(self, name, member_id, email):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.borrowed_books = []
        self.fees = 0.0
    
    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            return True
        return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            return True
        return False
    
    def search_match(self, query):
        return query.lower() in self.name.lower()