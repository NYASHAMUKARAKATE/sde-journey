from bank import BankAccount, SavingsAccount, BankStorage

def main():
    # Create accounts
    checking = BankAccount("Nyasha", 1000)
    savings = SavingsAccount("Nyasha", rate=0.05, starting_balance=5000)
    
    # Transactions
    checking.deposit(500)
    savings.add_interest()
    
    print(f"Checking balance: ${checking.balance:.2f}")
    print(f"Savings balance: ${savings.balance:.2f}")

if __name__ == "__main__":
    main()