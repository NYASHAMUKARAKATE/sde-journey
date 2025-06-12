class BankAccount:
    """This class define what the Account owner will do"""
    
    def __init__(self, name, starting_balance=0):
        self.owner = name
        self.balance = starting_balance
        self.history = []  # tracking all the transactions made by the user
        
    def deposit(self, amount):
        """Adding money to your bank account"""
        if amount <= 0:
            raise ValueError("You can't deposit negative money!")
        self.balance += amount
        self.history.append(f"Deposited is : ${amount}")
        
    def withdraw(self, amount):
        """Take money out (if you have enough money i the account)"""
        if amount > self.balance:
            raise ValueError("Oops - too broke for that!")
        self.balance -= amount
        self.history.append(f"Withdrown is : ${amount}")