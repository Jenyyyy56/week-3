class Person:
    # person has nmae
    def __init__(self, name:str):
        self.__name = name
        pass

    @property
    def name(self):
        return self.__name
    pass