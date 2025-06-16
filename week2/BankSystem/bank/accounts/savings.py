"""Special accounts that grow your money over time"""
from .core import BankAccount 
from ..accounts.core import BankAccount

class SavingsAccount(BankAccount):
    
    def __init__(self, name, rate=0.01, starting_balance=0):
        super().__init__(name, starting_balance)
        self.interest_rate = rate  # 1% growth per year
        
    def add_interest(self):
        """Free money! (Well, bank money)"""
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        self.history.append(f"Interest added: ${interest:.2f}")