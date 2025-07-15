class BankAccount:
    """Base bank account class"""
    
    def __init__(self, owner, starting_balance=0):
        self.owner = owner
        self.balance = starting_balance
        self.history = []
        
    def deposit(self, amount):
        """Add money to account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.history.append({
            'type': 'deposit',
            'amount': amount,
            'balance': self.balance,
            'timestamp': self._get_timestamp()
        })
        
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append({
            'type': 'withdrawal',
            'amount': amount,
            'balance': self.balance,
            'timestamp': self._get_timestamp()
        })
    
    def transfer(self, amount, recipient_account):
        """Transfer money to another account"""
        self.withdraw(amount)
        recipient_account.deposit(amount)
        self.history.append({
            'type': 'transfer_out',
            'amount': amount,
            'recipient': recipient_account.owner,
            'balance': self.balance,
            'timestamp': self._get_timestamp()
        })
        recipient_account.history.append({
            'type': 'transfer_in',
            'amount': amount,
            'sender': self.owner,
            'balance': recipient_account.balance,
            'timestamp': self._get_timestamp()
        })
    
    def _get_timestamp(self):
        """Helper method to get current timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")