def authenticate():
    real_pass = 1234
    password = int(input("Please enter your password to continue : "))
    
    if password == real_pass:
        print("You are successfully logged in")
        
    else:
        print("You have entered an invalid password")
        authenticate()
authenticate()

class BankAccount:
    """a base aacount thas has the deposit/withdraw functionallity"""
    def __init__(self, owner: str, balance: 0.0):
        self.owner = owner
        self._balance = balance
        self._transaction = [] # track history of the owner
        
    def deposit(self, amount: float):
        """This adds  the funds  an log transactions of the user"""
        if amount <= 0:
            raise ValueError("You shou enter a non negetive amount")
        self._balance += amount
        self._transaction.append(f"Your Deposit : +${amount:.2f}")
        
    def withdraw(self, amount: float):
        """Remove the funds if  the balance is sufficient"""
        if self._balance < amount:
            raise ValueError("You have insufficient funds")
        self._balance -= amount
        self._transaction.append(f"Your withdrawal is : -${amount:.2f}")
    
    def __str__(self):
        return f"Account({self.owner}, Balance= ${self._balance:.2f})"

#acc = BankAccount("Nyasha", 100.0)
#acc.deposit(50.0)
#acc.withdraw(25.0)
#print(acc)         
       
class SavingsAccount(BankAccount):
    """this Account earns interest but has withdrawal limits"""
    
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        """Using the monthly"""
        interest = self._balance * self.interest_rate
        self.deposit(interest)
    
    def withdraw(self, amount: float):  # Override parent method
        """Limit withdrawals to $500 per day"""
        if amount > 500:
            raise ValueError("Daily withdrawal limit exceeded")
        super().withdraw(amount)
        
#acc = SavingsAccount("Nyasha", 100.0)
#acc.deposit(50000.0)
#acc.withdraw(300.0)
#print(acc)  

def process_accounts(accounts: list[BankAccount]):
    """Handle many different account types uniformly"""
    for acc in accounts:
        if isinstance(acc, SavingsAccount):
            acc.add_interest()
        print(f"Processed: {acc}")
        
normal = BankAccount("Nyasha", 500.0)
savings = SavingsAccount("Mukarakate", 1000.0, 0.02)
process_accounts([normal, savings])  