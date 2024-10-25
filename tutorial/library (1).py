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
    
    def manage_books_menu(self):
        # TODO
        return
    def new_library_card_menu(self):
        # TODO
        return
    def manage_library_card_menu(self):
        # TODO
        return
    def close(self):
        print("Close and Save")
        return
    

    def add_book(self, book: Book):
        #used when purchasing a new book for the library
        self.__books.append(book)
        print("Adding", book)
        pass

    def remove_book(self, book: Book):
        #used when removing a book from the library
        self.__books.remove(book)
        pass

    def new_library_card(self, person: Person):
        new_library_card = Card(person)
        self.__library_cards.append(new_library_card)
        pass
    def deactive_library_card(self, library: Card):
        self.__library_cards.remove(library)
        pass

    def list_books(self):
        for book in self.__books:
            print(book)
            pass
        pass
    def list_patrons(self):
        for card in self.__library_cards:
            print(card)
            pass
        pass
    pass

Library()

