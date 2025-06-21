from bank import SavingsAccount, BankStorage
from bank.security.passwords import create_password, verify_password

def main():
    print("----------BANK SYSTEM WORKING ---------")
    storage = BankStorage()
    accounts = storage.load()

    while True:
        print("\n--- Main Menu ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Admin: List All Accounts")
        print("4. Admin: Delete Account")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            owner = input("Enter your name: ")
            if owner in accounts:
                print("Account already exists.")
                continue
            password = input("Set a password for your account: ")
            password_hash = create_password(password)
            try:
                starting_balance = float(input("Starting balance: "))
            except ValueError:
                print("Invalid amount.")
                continue
            rate = 0.05
            acc = SavingsAccount(owner, rate=rate, starting_balance=starting_balance)
            acc.password_hash = password_hash
            accounts[owner] = acc
            storage.save(accounts)
            print(f"Account created for {owner}.")

        elif choice == "2":
            owner = input("Enter your name: ")
            if owner not in accounts:
                print("Account not found.")
                continue
            password = input("Enter your password: ")
            acc = accounts[owner]
            if not verify_password(password, acc.password_hash):
                print("Incorrect password!")
                continue
            print(f"\nWelcome, {owner}!")
            while True:
                print("\n--- Account Menu ---")
                print("1. View Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Add Interest")
                print("5. View Transaction History")
                print("6. Delete Account")
                print("7. Logout")
                sub_choice = input("Choose an option: ")

                if sub_choice == "1":
                    print(f"Balance: ${acc.balance:.2f}")
                elif sub_choice == "2":
                    try:
                        amount = float(input("Deposit amount: "))
                        acc.deposit(amount)
                        print("Deposit successful.")
                    except Exception as e:
                        print(f"Error: {e}")
                elif sub_choice == "3":
                    try:
                        amount = float(input("Withdraw amount: "))
                        acc.withdraw(amount)
                        print("Withdrawal successful.")
                    except Exception as e:
                        print(f"Error: {e}")
                elif sub_choice == "4":
                    interest = acc.add_interest()
                    print(f"Interest added: ${interest:.2f}")
                elif sub_choice == "5":
                    print("Transaction History:")
                    for item in acc.history[-10:]:
                        print(" -", item)
                elif sub_choice == "6":
                    confirm = input("Are you sure you want to delete your account? (yes/no): ")
                    if confirm.lower() == "yes":
                        del accounts[owner]
                        storage.save(accounts)
                        print("Account deleted.")
                        break
                elif sub_choice == "7":
                    storage.save(accounts)
                    print("Logged out.")
                    break
                else:
                    print("Invalid option.")
            storage.save(accounts)

        elif choice == "3":
            print("All accounts:")
            for owner in accounts:
                print(f"- {owner}")
        elif choice == "4":
            admin_name = input("Admin name: ")
            admin_pass = input("Admin password: ")
            # Simple admin check (replace with real admin logic as needed)
            if admin_name == "admin" and admin_pass == "admin123":
                del_name = input("Enter account name to delete: ")
                if del_name in accounts:
                    del accounts[del_name]
                    storage.save(accounts)
                    print(f"Deleted account {del_name}.")
                else:
                    print("Account not found.")
            else:
                print("Admin authentication failed.")
        elif choice == "5":
            storage.save(accounts)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()