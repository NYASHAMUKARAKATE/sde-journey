class BankAccount:
    """This class define what the Account owner will do"""
    
    def __init__(self, owner, starting_balance=0):
        self.owner = owner
        self.balance = starting_balance
        self.history = []  # tracking all the transactions made by the user
        
    def deposit(self, amount):
        """Adding money to your bank account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.history.append(f"Deposited ${amount:.2f}")
        
    def withdraw(self, amount):
        """Take money out (if you have enough money i the account)"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(f"Withdrew ${amount:.2f}")