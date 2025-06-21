import json
import os
from member import Member
from book import Book

class Database:
    def __init__(self, file="library_data.json"):
        self.file = file
        self.books = []
        self.members = []
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.file):
            try:
                with open(self.file, 'r') as f:
                    data = json.load(f)
                    self.books = [Book.from_dict(b) for b in data.get('books', [])]
                    self.members = [Member.from_dict(m) for m in data.get('members', [])]
            except json.JSONDecodeError:
                print("Warning: Data file corrupted, starting fresh")
    
    def save_data(self):
        data = {
            'books': [b.to_dict() for b in self.books],
            'members': [m.to_dict() for m in self.members]
        }
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_book(self, book):
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError("Book with this ISBN already exists")
        self.books.append(book)
    
    def add_member(self, member):
        if any(m.member_id == member.member_id for m in self.members):
            raise ValueError("Member with this ID already exists")
        self.members.append(member)
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def delete_book(self, isbn):
        self.books = [b for b in self.books if b.isbn != isbn]
    
    def delete_member(self, member_id):
        self.members = [m for m in self.members if m.member_id != member_id]