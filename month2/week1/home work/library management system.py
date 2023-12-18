import datetime
class Book:
    def __init__(self, title, author, ISBN, A_status):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.A_status = A_status
    
    def display_book_details(self):
        print(f"Book title: {self.title}\nBook author: {self.author}\nBook ISBN: {self.ISPN} \nBook availability status: {self.A_status}")
    
    def update_A_status(self,update):
        self.A_status = update
        return self.A_status

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_user_detail(self):
        print(f"User ID: {self.user_id}\nUser Name: {self.name}\nBook Borrowed: {self.books_borrowed} \n") 

    def borrow_book(self,book):
        if book.A_status == "Available":
            self.books_borrowed.append(book.title)
            book.update_A_status("Borrowed")
            return f"{self.name} has borrowed {book.title}"
        else:
            return "Sorry, This book is not available"

    def return_book(self, book):
        if book.title in self.books_borrowed:
            self.books_borrowed.remove(book.title)
            book.update_A_status("Available")   
            return  f"{self.name} has returned {book.title}"
        else:
            return "Sorry, this book was not borrowed by this user."
    
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self,book):
        self.books.append(book)
    
    def add_user(self,user):
        self.users.append(user)
    
    def handle_book_transaction(self, user, book, borrow = True):
        if borrow:
            self.borrow_book(book)
        else:
            self.return_book(book)

class Transaction:
    def __init__(self, user, book, transaction_type):
        self.user = user
        self.book = book
        self.transaction_type = transaction_type
        self.time = datetime.datetime.now()
    
    def record_transactions(self):
        return f"User: {self.user.name}, Book: {self.book.title}, Transaction Type: {self.transaction_type}, Date: {self.date}"

    def generate_report(self):
        return self.record_transactions()

class CLI:
    def __init__(self, Library):
        self.library = Library
    
    def Add_books(self):
        title = input("Book title: ")
        author = input("Book author")
        ISBN = input("Book ISBN:")
        status = input("Book status: ")
        book = Book(title,author,ISBN,status)
        self.library.add_book(book)

    def register_user(self):
        user_id = input("User ID: ")
        name = input("User name: ")
        user = User(user_id, name)
        self.library.add_user(user)


    def borrow_book(self):
        user_id = input("User ID: ")
        ISBN = input("Book ISBN: ")
        user = next((user for user in self.library.users if self.library.user_id == user_id), None)
        book = next((book for book in self.library.books if self.library.ISBN == ISBN), None)

        if user and book:
            book.borrow_book(book)
            transaction = Transaction(user, book, "Borrow")
            print(transaction.generate_report())

    def return_book(self):
        user_id = input("User ID: ")
        ISBN = input("Book ISBN: ")
        user = next((user for user in self.library.users if self.library.user_id == user_id), None)
        book = next((book for book in self.library.books if self.library.ISBN == ISBN), None)

        if user and book:
            book.return_book(book)
            transaction = Transaction(user, book, "Return")
            print(transaction.generate_report())                

    def review_report(self):
        for user in self.library.users:
            print(user.display_user_detail())
        for book in self.library.books:
            print(book.display_book_details())
    







    