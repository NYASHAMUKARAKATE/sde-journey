from bank import BankAccount, SavingsAccount, BankStorage
from bank.security.passwords import create_password, check_password

def main():
    # Setup
    storage = BankStorage()
    accounts = storage.load() or {}
    
    # Open new account
    if "nyasha" not in accounts:
        nyasha_acc = SavingsAccount("Nyasha", rate=0.05, starting_balance=1000)
        nyasha_acc.password_hash = create_password("secure123")
        accounts["nyasha"] = nyasha_acc
    
    # Monthly interest
    accounts["nyasha"].add_interest()
    
    # Save everything
    storage.save(accounts)
    
    print(f"Nyasha's balance: ${accounts['nyasha'].balance:.2f}")
    print("Recent activity:", accounts["nyasha"].history[-2:])

if __name__ == "__main__":
    main()