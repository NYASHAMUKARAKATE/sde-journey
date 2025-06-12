"""this will let you run the bank account"""

from bank.accounts.core import BankAccount
from bank.security.passwords import create_password

# Openning a new account
my_account = BankAccount("Nyasha", 100)

my_account.deposit(50)
print(f"Balance: ${my_account.balance}")
print("Recent activity:", my_account.history[-1])