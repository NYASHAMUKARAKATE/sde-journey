from bank.accounts.core import BankAccount
from bank.accounts.savings import SavingsAccount
from bank.database.storage import BankStorage
from bank.security.passwords import create_password

def main():
    # Setup
    storage = BankStorage()
    accounts = storage.load() or {}

    # Open new account if not exists
    if "nyasha" not in accounts:
        nyasha_acc = SavingsAccount("Nyasha", rate=0.05, starting_balance=1000)
        nyasha_acc.password_hash = create_password("secure123")
        accounts["nyasha"] = nyasha_acc

    # Monthly interest
    if hasattr(accounts["nyasha"], "add_interest"):
        accounts["nyasha"].add_interest()
    else:
        print("Error: add_interest method missing.")

    # Save everything
    storage.save(accounts)

    # Print balance and recent activity
    balance = getattr(accounts["nyasha"], "balance", None)
    history = getattr(accounts["nyasha"], "history", [])
    print(f"Nyasha's balance: ${balance:.2f}" if balance is not None else "Balance not found.")
    print("Recent activity:", history[-2:])

if __name__ == "__main__":
    main()