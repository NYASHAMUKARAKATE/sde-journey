from library import Library

def main():
    lib = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Register Member")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. List Overdue Books")
        print("7. Admin: List All Members")
        print("8. Admin: Delete Book")
        print("9. Admin: Delete Member")
        print("10. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            member = lib.register_member(name, email)
            print(f"Registered {name} with ID {member.member_id}")

        elif choice == "2":
            title = input("Book Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            try:
                lib.add_new_book(title, author, isbn)
                print("Book added.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            print(lib.borrow_book(member_id, isbn))

        elif choice == "4":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            print(lib.return_book(member_id, isbn))

        elif choice == "5":
            query = input("Search query: ")
            results = lib.search_books(query)
            if results:
                for book in results:
                    print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {'Available' if book.is_available else 'Checked out'}")
            else:
                print("No books found.")

        elif choice == "6":
            overdue = lib.list_overdue_books()
            if overdue:
                for book in overdue:
                    print(f"{book.title} (ISBN: {book.isbn}) is overdue!")
            else:
                print("No overdue books.")

        elif choice == "7":
            members = lib.list_members()
            for m in members:
                print(f"{m.name} (ID: {m.member_id}, Email: {m.email}, Fees: ${m.fees:.2f})")

        elif choice == "8":
            isbn = input("ISBN of book to delete: ")
            lib.delete_book(isbn)
            print("Book deleted.")

        elif choice == "9":
            member_id = input("Member ID to delete: ")
            lib.delete_member(member_id)
            print("Member deleted.")

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()