class Book:
    # books havae a title
    # books have authors, which are people
    # library books have a loan status(are they out on loan?)

    def __init__(self, title: str, authors: list, year: int) -> None:
        self.title = title
        self.authors = authors
        self.year = year
        self.loan_status = False
        pass

    @property
    def title(self):
        return self._title
    
    @property
    def authors(self):
        return self._authors
    
    @property
    def year(self):
        return self._year
    
    @property
    def loan_status(self):
        return self._loan_status
    
    def return_book(self):
        self.loan_status = False
        pass

    def borrow_book(self):
        self.loan_status = True
        pass

    def __str__(self) -> str:
        values = [
            self.title,
            ",".join(self.authors),
            "("+str(self.year)+")",
            str(self.loan_status)
        ]
        return "\t".join(values)
    pass
