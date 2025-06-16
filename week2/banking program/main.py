# a simple banking program

def deposit():
    amount = float(input("Enter the amount to deposit: $"))
    
    if amount <= 0:
        print("OOPS that was not a valid amount. Please enter a positive number.")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount to withdraw: $"))
    
    if amount > balance:
        print("OOPS you cannot withdraw more than your current balance.")
        return 0
    elif amount <= 0:
        print("OOPS that was not a valid amount. Please enter a positive number.")
        return 0
    else:
        return amount

def show_balance():
    print(f"\nYour current balance is: ${balance:.2f}")

# Main function to run the banking program
def main():
    global balance
    balance = 0
    is_running = True

    while is_running:
        print("\n--- Banking Program ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Enter the choice you want (1-4): ")

        if choice == '1':
            balance += deposit()
        elif choice == '2':
            balance -= withdraw()
        elif choice == '3':
            show_balance()
        elif choice == '4':
            print("Exiting the program.")
            is_running = False
        else:
            print("\n......You have entered an incorrect choice, please try again.")

    print("\n Thank you , have a great day!")
    
if __name__ == "__main__":
    main()