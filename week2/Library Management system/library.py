from database import Database
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.db = Database()
    
    def add_new_book(self, title, author, isbn):
    
        new_book = Book(title, author, isbn)
        self.db.add_book(new_book)
        self.db.save_data()
        return new_book
    
    def register_member(self, name, email):
       
        member_id = f"M{len(self.db.members) + 1:04d}"
        new_member = Member(name, member_id, email)
        self.db.add_member(new_member)
        self.db.save_data()
        return new_member
    
    def borrow_book(self, member_id, isbn):
        member = self.db.find_member(member_id)
        book = self.db.find_book(isbn)
        
        if not member or not book:
            return "Member or book not found"
        
        if member.borrow_book(book):
            self.db.save_data()
            return f"{book.title} borrowed by {member.name}"
        return "Book not available"
    
    def return_book(self, member_id, isbn):
        member = self.db.find_member(member_id)
        book = self.db.find_book(isbn)
        
        if not member or not book:
            return "Member or book not found"
        
        if member.return_book(book):
            self.db.save_data()
            return f"{book.title} returned by {member.name}"
        return "Book not borrowed by this member"
    
    
    def search_books(self, query):
        return [book for book in self.db.books if book.search_match(query)]
    
    
    def list_overdue_books(self):
        return []  # Placeholder - not implemented yet