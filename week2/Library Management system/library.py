from database import Database
from book import Book
from member import Member
import helpers

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
        if not book.is_available:
            return "Book not available"
        if member.borrow_book(book):
            book.checkout()
            self.db.save_data()
            return f"{book.title} borrowed by {member.name}. Due: {book.due_date.strftime('%Y-%m-%d')}"
        return "Book not available"

    def return_book(self, member_id, isbn):
        member = self.db.find_member(member_id)
        book = self.db.find_book(isbn)
        if not member or not book:
            return "Member or book not found"
        if member.return_book(book):
            book.return_book()
            fee_msg = ""
            if book.return_date and book.due_date and book.return_date > book.due_date:
                days_overdue = (book.return_date - book.due_date).days
                fee = helpers.calculate_fees(days_overdue)
                member.fees += fee
                fee_msg = f" and ${fee:.2f} late fee has been applied"
                if days_overdue > 7:
                    helpers.send_reminder_email(member, book, days_overdue)
            self.db.save_data()
            return f"{book.title} returned by {member.name}{fee_msg}"
        return "Book not borrowed by this member"

    def search_books(self, query):
        return [book for book in self.db.books if book.search_match(query)]

    def list_overdue_books(self):
        from datetime import datetime
        overdue = []
        for book in self.db.books:
            if not book.is_available and book.due_date and book.due_date < datetime.now():
                overdue.append(book)
        return overdue

    def list_members(self):
        return self.db.members

    def delete_book(self, isbn):
        self.db.delete_book(isbn)
        self.db.save_data()

    def delete_member(self, member_id):
        self.db.delete_member(member_id)
        self.db.save_data()