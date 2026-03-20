class Book:
    def __init__(self, book_id, name):
        self.book_id = book_id
        self.name = name
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        self.books.append(Book(book_id, name))
        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return
        for b in self.books:
            status = "Issued" if b.is_issued else "Available"
            print(f"{b.book_id} - {b.name} ({status})")

    def issue_book(self):
        book_id = int(input("Enter Book ID to issue: "))
        for b in self.books:
            if b.book_id == book_id and not b.is_issued:
                b.is_issued = True
                print("Book issued successfully!")
                return
        print("Book not available!")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))
        for b in self.books:
            if b.book_id == book_id and b.is_issued:
                b.is_issued = False
                print("Book returned successfully!")
                return
        print("Invalid return!")


# Menu-driven program
lib = Library()

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        lib.add_book()
    elif choice == 2:
        lib.display_books()
    elif choice == 3:
        lib.issue_book()
    elif choice == 4:
        lib.return_book()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")