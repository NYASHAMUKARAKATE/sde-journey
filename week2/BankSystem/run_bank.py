from bank import SavingsAccount, BankStorage

def main():
    print("----------BANK SYSTEM WORKING ---------")
    
    # Create savings account
    nyasha_acc = SavingsAccount("Nyasha", rate=0.05, starting_balance=10)
    print(f"Created account for {nyasha_acc.owner}")
    print(f"Initial balance: ${nyasha_acc.balance:.2f}")
    
    # Add interest
    try:
        interest = nyasha_acc.add_interest()
        print(f"Added interest: ${interest:.2f}")
        print(f"New balance: ${nyasha_acc.balance:.2f}")
    except TypeError:
        print("⚠️ Interest calculation failed - using fallback")
        print(f"Current balance: ${nyasha_acc.balance:.2f}")
    
    # Save to storage
    storage = BankStorage()
    if storage.save({"nyasha": nyasha_acc}):
        print("Account saved successfully!")
    else:
        print("⚠️ Failed to save account")

if __name__ == "__main__":
    main()