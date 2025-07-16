from flask import Flask, render_template, request, redirect, url_for, flash
from library import Library
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
lib = Library()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Get some stats for the dashboard
    total_books = len(lib.db.books)
    available_books = len([b for b in lib.db.books if b.is_available])
    total_members = len(lib.db.members)
    overdue_books = len(lib.list_overdue_books())
    
    return render_template('dashboard.html', 
                         total_books=total_books,
                         available_books=available_books,
                         total_members=total_members,
                         overdue_books=overdue_books)

@app.route('/members')
def list_members():
    members = lib.list_members()
    return render_template('members.html', members=members)

@app.route('/members/register', methods=['GET', 'POST'])
def register_member():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        try:
            member = lib.register_member(name, email)
            flash(f'Member {name} registered with ID {member.member_id}', 'success')
            return redirect(url_for('list_members'))
        except Exception as e:
            flash(str(e), 'danger')
    return render_template('register_member.html')

@app.route('/books')
def list_books():
    books = lib.db.books
    return render_template('books.html', books=books)

@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        try:
            lib.add_new_book(title, author, isbn)
            flash('Book added successfully', 'success')
            return redirect(url_for('list_books'))
        except Exception as e:
            flash(str(e), 'danger')
    return render_template('add_book.html')

@app.route('/books/borrow', methods=['GET', 'POST'])
def borrow_book():
    if request.method == 'POST':
        member_id = request.form['member_id']
        isbn = request.form['isbn']
        result = lib.borrow_book(member_id, isbn)
        flash(result, 'success' if 'borrowed' in result else 'danger')
        return redirect(url_for('list_books'))
    
    members = lib.list_members()
    available_books = [b for b in lib.db.books if b.is_available]
    return render_template('borrow_book.html', 
                         members=members, 
                         books=available_books)

@app.route('/books/return', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        member_id = request.form['member_id']
        isbn = request.form['isbn']
        result = lib.return_book(member_id, isbn)
        flash(result, 'success' if 'returned' in result else 'danger')
        return redirect(url_for('list_books'))
    
    members = lib.list_members()
    borrowed_books = [b for b in lib.db.books if not b.is_available]
    return render_template('return_book.html', 
                         members=members, 
                         books=borrowed_books)

@app.route('/books/search')
def search_books():
    query = request.args.get('query', '')
    results = lib.search_books(query)
    return render_template('search_books.html', 
                         books=results, 
                         query=query)

@app.route('/books/overdue')
def overdue_books():
    overdue = lib.list_overdue_books()
    return render_template('overdue_books.html', 
                         books=overdue)

@app.route('/books/delete', methods=['POST'])
def delete_book():
    isbn = request.form['isbn']
    lib.delete_book(isbn)
    flash('Book deleted successfully', 'success')
    return redirect(url_for('list_books'))

@app.route('/members/delete', methods=['POST'])
def delete_member():
    member_id = request.form['member_id']
    lib.delete_member(member_id)
    flash('Member deleted successfully', 'success')
    return redirect(url_for('list_members'))

if __name__ == '__main__':
    app.run(debug=True)