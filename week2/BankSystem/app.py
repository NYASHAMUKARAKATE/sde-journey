from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from bank.core import BankAccount
from bank.savings import SavingsAccount
from bank.storage import BankStorage
from bank.passwords import create_password, verify_password
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minute session timeout

storage = BankStorage()
accounts = storage.load()


def get_current_account():
    if 'username' not in session:
        return None
    return accounts.get(session['username'])

def is_admin():
    return session.get('username') == 'admin'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        owner = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if owner in accounts:
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('register'))
            
        if len(password) < 8:
            flash('Password must be at least 8 characters', 'error')
            return redirect(url_for('register'))
        
        try:
            starting_balance = float(request.form.get('balance', 0))
        except ValueError:
            starting_balance = 0
            
        password_hash = create_password(password)
        acc = SavingsAccount(owner, rate=0.05, starting_balance=starting_balance)
        acc.password_hash = password_hash
        accounts[owner] = acc
        storage.save(accounts)
        
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        owner = request.form['username']
        password = request.form['password']
        
        if owner not in accounts:
            flash('Account not found', 'error')
            return redirect(url_for('login'))
        
        acc = accounts[owner]
        if not verify_password(password, acc.password_hash):
            flash('Incorrect password', 'error')
            return redirect(url_for('login'))
            
        session['username'] = owner
        session['last_activity'] = datetime.now().timestamp()
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    account = get_current_account()
    if not account:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', account=account)

@app.route('/deposit', methods=['POST'])
def deposit():
    account = get_current_account()
    if not account:
        return redirect(url_for('login'))
    
    try:
        amount = float(request.form['amount'])
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        account.deposit(amount)
        storage.save(accounts)
        flash(f'Successfully deposited ${amount:.2f}', 'success')
    except ValueError as e:
        flash(str(e), 'error')
    
    return redirect(url_for('dashboard'))

@app.route('/withdraw', methods=['POST'])
def withdraw():
    account = get_current_account()
    if not account:
        return redirect(url_for('login'))
    
    try:
        amount = float(request.form['amount'])
        account.withdraw(amount)
        storage.save(accounts)
        flash(f'Successfully withdrew ${amount:.2f}', 'success')
    except ValueError as e:
        flash(str(e), 'error')
    
    return redirect(url_for('dashboard'))

@app.route('/transfer', methods=['POST'])
def transfer():
    account = get_current_account()
    if not account:
        return redirect(url_for('login'))
    
    try:
        amount = float(request.form['amount'])
        recipient = request.form['recipient']
        
        if recipient not in accounts:
            raise ValueError("Recipient account not found")
        if account.owner == recipient:
            raise ValueError("Cannot transfer to yourself")
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        recipient_account = accounts[recipient]
        account.transfer(amount, recipient_account)
        storage.save(accounts)
        
        flash(f'Transferred ${amount:.2f} to {recipient}', 'success')
    except ValueError as e:
        flash(str(e), 'error')
    
    return redirect(url_for('dashboard'))

@app.route('/transactions')
def transactions():
    account = get_current_account()
    if not account:
        return redirect(url_for('login'))
    
    return render_template('transactions.html', account=account)

@app.route('/admin')
def admin_panel():
    if not is_admin():
        flash('Admin access required', 'error')
        return redirect(url_for('login'))
    
    return render_template('admin.html', accounts=accounts)

@app.route('/admin/delete/<username>')
def admin_delete(username):
    if not is_admin():
        flash('Admin access required', 'error')
        return redirect(url_for('login'))
    
    if username in accounts:
        del accounts[username]
        storage.save(accounts)
        flash(f'Deleted account: {username}', 'success')
    else:
        flash('Account not found', 'error')
    
    return redirect(url_for('admin_panel'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)