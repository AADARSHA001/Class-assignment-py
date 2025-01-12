# 4. Basic Library Management System
# Objective: Create a system to manage book borrowing.
# Steps:
# 1. Use a list to store available books (e.g., ["Book1", "Book2"]).
# 2. Display a menu:
# o View books.
# o Borrow a book (remove from the list if available).
# o Return a book (add to the list if not already in it).
# o Exit.
# 3. Keep the program running in a loop until the user exits.
# 4. Use functions for each operation to organize the code.


def display_books(books):
    """Display the list of available books."""
    if books:
        print("\nAvailable Books:")
        for book in books:
            print(f"- {book}")
    else:
        print("\nNo books are currently available.")

def borrow_book(books, borrowed_books):
    """Allow the user to borrow a book."""
    book_to_borrow = input("\nEnter the name of the book you want to borrow: ").strip()
    if book_to_borrow in books:
        books.remove(book_to_borrow)
        borrowed_books.append(book_to_borrow)
        print(f"You have borrowed '{book_to_borrow}'.")
    else:
        print(f"Sorry, '{book_to_borrow}' is not available or doesn't exist.")

def return_book(books, borrowed_books):
    """Allow the user to return a borrowed book."""
    book_to_return = input("\nEnter the name of the book you want to return: ").strip()
    if book_to_return in borrowed_books:
        borrowed_books.remove(book_to_return)
        if book_to_return not in books:
            books.append(book_to_return)
        print(f"Thank you for returning '{book_to_return}'.")
    else:
        print(f"'{book_to_return}' was not borrowed from this library.")

def library_management_system():
    """Main function to run the library management system."""
    books = ["Book1", "Book2", "Book3", "Book4"]
    borrowed_books = []
    
    while True:
        print("\nLibrary Management System")
        print("1. View Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            display_books(books)
        elif choice == "2":
            borrow_book(books, borrowed_books)
        elif choice == "3":
            return_book(books, borrowed_books)
        elif choice == "4":
            print("\nThank you for using the Library Management System!")
            break
        else:
            print("\nInvalid choice. Please select an option from 1 to 4.")

# Run the library management system
library_management_system()
