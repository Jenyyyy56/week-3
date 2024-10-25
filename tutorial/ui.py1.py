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

class Menu:
    '''
    Menu has a list of Menu Items.
    Menu has a name, which is a string.
    '''
    def __init__(self, name: str, options) -> None:
        self.__name = name
        self.__options = options
        self.display()
        pass

    @property
    def name(self):
        return self.__name
    @property
    def options(self):
        return self.__options
    
    def display(self):
        print()
        print(self.name.upper())# make sure the menu is in capitilize
        for option in self.options:
            #displays the menu
            index = self.options.index(option)
            index = index + 1
            name = option.name
            print(index, name)
            pass
        self.input() # call the iinput method, to be interactive
        return
    def input(self):
        # handles all input, with exception handling
        user_input = input("Please enter a number: ")
        try:
            index = int(user_input)
            index = index - 1
            option = self.options[index]
            parameters = option.parameters

            if parameters is None:
                option.method() # the correct method is called 
                return
            
            else:
                #unpack the paramters 
                if len(parameters) > 0:
                    option.method(*parameters) # need to use *parameters
                    return
                else:
                    option.method(parameters)
                    return
        except Exception as e:
            print(e) # display the error 
            self.run() # rerun the menu
            pass
        return
    pass
    