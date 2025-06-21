from .core import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, rate=0.01, starting_balance=0):
        super().__init__(owner, starting_balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.balance += interest
        self.history.append(f"Interest added: ${interest:.2f}")
        return interest