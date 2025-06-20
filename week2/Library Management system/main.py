from library import Library
from book import Book
from member import Member

def main():
    lib = Library()

    
    if not lib.db.find_book("9780743273565"):
        lib.add_new_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    if not lib.db.find_book("9780446310789"):
        lib.add_new_book("To Kill a Mockingbird", "Harper Lee", "9780446310789")

    if not lib.db.find_member("M0001"):
        lib.register_member("Nyasha Mukarakkate", "nyasha@gmail.com")
    if not lib.db.find_member("M0002"):
        lib.register_member("Bob Muks", "bob@gmail.com")
    
    print("\n-----------Library System --------")
    print("1. Search Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Add New Member")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            query = input("Search books: ")
            results = lib.search_books(query)
            for book in results:
                print(f"- {book}")
        
        elif choice == "2":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            print(lib.borrow_book(member_id, isbn))
        
        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            print(lib.return_book(member_id, isbn))
        
        elif choice == "4":
            name = input("Name: ")
            email = input("Email: ")
            member = lib.register_member(name, email)
            print(f"Registered {name} with ID {member.member_id}")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("oops you have entered an invalid choice, try again")

if __name__ == "__main__":
    main()