Library_books_list = []
borrowed_books = {}

class Library:
    def __init__(self, book_name):
        self.book_name = book_name

    def submit_book(self):
        book = self.book_name
        Library_books_list.append(book)
        print(f"{book} has been submitted to the library. ")
    
    def display_books(self):
        if Library_books_list == []:
            print("No books in the library.")
        else:
            print("Books available in the library:")
            print("\n".join(Library_books_list))
    
    def check_book(self):
        book = self.book_name   
        if book in Library_books_list:
            print(f"{book} is available in the library.")
        else:
            print(f"{book} is not available in the library.")
    
    def borrow_book(self):
        book = self.book_name
        if book not in Library_books_list:
            print(f"{book} is currently not available in the library.")
        elif book in borrowed_books:
            print(f"{book} is already borrowed by {borrowed_books[book]}.")
        else:
            name = input("Enter your name: ")
            borrowed_books.update({book:name})
            Library_books_list.remove(book)
            print(f"{book} has been borrowed by {name}.")

while True:
    print("               WELCOME TO KJ LIBRARY")
    print("Do you want to Submit a book, Display book list, Check book availability or Borrow a book?")
    user_input = input("Enter your choice (Submit, Display, Check, Borrow): ").lower()
    if user_input == "submit":
        book_name = input("Enter the name of the book you want to submit:")
        submitter_name = input("Enter your name: ")
        library = Library(book_name)
        library.submit_book()
        if book_name in borrowed_books.keys():
            borrowed_books.pop(book_name)
    elif user_input == "display":
        library = Library("")
        library.display_books()
    elif user_input == "check":
        library = Library(input("Enter the name of the book you want to check: "))
        library.check_book()
    elif user_input == "borrow":
        library = Library(input("Enter the name of the book you want to borrow: "))
        library.borrow_book()
    else:
        print("Invalid choice. Please try again.")
    print(borrowed_books)
