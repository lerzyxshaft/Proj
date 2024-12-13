from ctypes.util import find_library


class Book: #Book class
    def __init__(self, title, autor, available, prod_date,):
        self.title = title
        self.autor = autor
        self.available = True
        self.prod_date = prod_date

    def available_status(self):    #Check available
        self.available = not self.available

class Library:  #Library class
    def __init__(self):
        self.books = []

    def add_book(self, book):    #New book
        self.books.append(book)

    def show_books(self):   #Show all Libraries books
        if not self.books:
            print('Our library is empty ')
        for book in self.books:
            print(book)

    def find_book(self, title): #find book
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def lend_book(self, title):
        book = self.find_book(title)
        if book and book.is_available:
            book.change_status()
            print(f"Book '{title}' was already taken.")
        elif book:
            print(f"Book '{title}' was already taken.")
        else:
            print(f"We don't have '{title}' in our library.")

    def return_book(self, title):
        book = self.find_book(title)
        if book and not book.is_available:
            book.change_status()
            print(f"Book  '{title}' was returned.")
        elif book:
            print(f"Book '{title}' already available.")
        else:
            print(f"Book '{title}' didn't found.")

def main(self):
    library = Library()
    while True:
        print("\n1. Show all boks")
        print("2. Find book")
        print("3. Lend book")
        print("4. Return book")
        print("5. Add book")
        print("6. Exit")
        choice = input("Choose what you want to do: ")

        if choice == 1:
            library.show_books()
        elif choice == 2:
            title = input('Fill this gap with name of book')
            book = library.find_book(title)
            print(book if book else 'We dont have this book')
        elif choice == 3:
            title = input('Fill this gap with name of book')
            library.lend_book(title)
        elif choice == 4:
            title = input('Fill this gap with name of book')
            library.return_book(title)
        elif choice == 5:
            title = input('Enter book title: ')
            prod_date = input('Enter when book was produced: ')
            autor = input('Enter autor of book: ')
            Library.add_book(Book(title, prod_date, autor))
            print('Book was added')
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Try one more time)")