from person import Person
from book import Book

class  Card:
    # cards are used to keep tract of borrowered books
    # caed must have a person (this would be a composition relationship)
    # card can have a books (this would be an aggeration relationship)

    def __init__(self, person: Person) -> None:
        self.__person = person
        self.__books = list()
        pass
    @property
    def person(self):
        return self.__person
    
    def borrow_book(self, book: Book):
        self.__books.append(book)
        pass

    def return_book(self, book: Book):
        self.__books.remove(book)
        pass
    pass