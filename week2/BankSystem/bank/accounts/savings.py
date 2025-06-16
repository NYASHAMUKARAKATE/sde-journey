from .core import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, rate=0.01, starting_balance=0):
        super().__init__(name, starting_balance)
        self.interest_rate = rate
        
    def add_interest(self):
        """Calculate and add interest, returns interest amount"""
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return interest