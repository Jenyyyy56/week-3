from card import Card
from book import Book
from person import Person
from ui import Menu, MenuItem

class Library:
    # library has books
    # libray has cards, to keep track of where the books are

    def __init__(self) -> None:
        self.__books = list()
        self.__library_cards = list()
        self.home_menu() # use the ui classes to cerate a home menu
        pass
    def home_menu(self):
        # create options to add and remove books
        # create options to add and remove cards
        name = "Library Home Menu"
        options = [
            MenuItem("New Book", self. new_book_menu),
            MenuItem("Manage Books", self.manage_books_menu),
            MenuItem("New Library card", self.new_library_card_menu),
            MenuItem("Manage Library cards", self.manage_library_card_menu),
            MenuItem("Close and save", self.close),
        ]
        Menu(name, options)
        return
    
    def new_book_menu(self):
        # TODO
        print("New Book")
        title = input("Title: ")
        authors = input("Authors (seperate by comas): ")
        year = input("Year: ")
        author_names = authors.split(",")
        authors = [Person(author_name) for author_name in author_names]
        book = Book(title, authors, year)
        self.add_book(book)
        self.home_menu()
        return
    
    