class Card:
    def __init__(self, name, value, suit) -> None:
        self.__name= name
        self.__value= value
        self.__suit= suit
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_value(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value
    
    def set_suit(self, suit):
        self.__suit = suit
    
    def get_suit(self):
        return self.__suit