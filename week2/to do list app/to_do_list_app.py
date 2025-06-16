# This is a simple to-do list app that allows users to add, remove, and view items in their to-do list.
# It uses a list to store the items and provides a simple text-based interface for interaction.
# The app runs in a loop until the user chooses to exit, allowing for multiple operations in one session.
# The app is designed to be user-friendly and provides feedback for each action taken.
# The app can be extended with features like saving the list to a file, loading from a file, or adding due dates for items.

my_list = []
def add_item(item):
    """Add an item to the to-do list."""
    my_list.append(item)
    print(f"Added: {item}")
    
def remove_item(item):
    """Remove an item from the to-do list."""
    if item in my_list:
        my_list.remove(item)
        print(f"Removed: {item}")
    else:
        print(f"Item not found: {item}")

def view_items():
    """View all items in the to-do list."""
    if my_list:
        print("-------------To-Do List:----------------")
        for item in my_list:
            print(f" - {item}")
    else:
        print("To-Do List is empty.You can add items using option 1.")
def main():
    while True:
        print("\n-----------To-Do List App------------\n")
        print("1. Add item")
        print("2. Remove item")
        print("3. View items")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            view_items()
        elif choice == '4':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice, please try again!!.")
            
if __name__ == "__main__":
    main()
    

            