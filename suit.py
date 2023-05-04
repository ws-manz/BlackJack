class Suit:
    def __init__(self, name, symbol) -> None:
        self.__name=name
        self.__symbol=symbol
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_symbol(self, symbol):
        self.__symbol = symbol
    
    def get_symbol(self):
        return self.__symbol

'''♠ ♥ ♦ ♣'''