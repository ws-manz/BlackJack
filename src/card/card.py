import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from card.suit import Suit

class Card:
    def __init__(self, name, value, suit: Suit) -> None:
        self.__name = name
        self.__value = value
        self.__suit = suit
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    @property
    def suit(self) -> Suit:
        return self.__suit
    
    @suit.setter
    def suit(self, suit: Suit):
        self.__suit = suit
    
    def __str__(self) -> str:
        return f"{self.__name} of {self.__suit}"
    
    def __eq__(self, other: 'Card') -> bool:
        return self.__value == other.get_value() and self.__suit == other.get_suit()
