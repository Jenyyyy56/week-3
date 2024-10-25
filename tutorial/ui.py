class MenuItem:
    '''
    Menu Item have a name and method
    Menu Items is a way of keeping the name and method together.
    Menu Items can store parameters if necessary
    '''

    def __init__(self, name:str, method, paramters = None) ->  None:
        self.__name = name
        self.__method = method
        self.__parameters = paramters
        pass
    @property
    def name(self):
        return self.__name
    @property
    def method(self):
        return self.__method
    @property
    def parameters(self):
        return self.__parameters
    pass

