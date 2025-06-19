import json
import os

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
                    self.books = [Book(**b) for b in data.get('books', [])]
                    self.members = [Member(**m) for m in data.get('members', [])]
            except json.JSONDecodeError:
                print("Warning: Data file corrupted, starting fresh")
    
    def save_data(self):
        data = {
            'books': [vars(b) for b in self.books],
            'members': [vars(m) for m in self.members]
        }
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=2)
    
    # Might not check for duplicates properly
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
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