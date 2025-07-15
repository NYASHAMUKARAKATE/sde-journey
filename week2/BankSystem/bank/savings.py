from .core import BankAccount

class SavingsAccount(BankAccount):
    """Savings account with interest"""
    
    def __init__(self, owner, rate=0.01, starting_balance=0):
        super().__init__(owner, starting_balance)
        self.rate = rate
    
    def add_interest(self):
        """Add interest to account"""
        interest = self.balance * self.rate
        self.balance += interest
        self.history.append({
            'type': 'interest',
            'amount': interest,
            'balance': self.balance,
            'timestamp': self._get_timestamp()
        })
        return interest