import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from card.suit import Suit
from card.card import Card

from card.card import Card
from card.suit import Suit
import random

class Deck:
    def __init__(self):
        self.__cards = self.__create_deck()
        self.__card_iterator = iter(self.__cards)

    def __create_suits(self):
        suits = [("spade", "♠"), ("heart", "♥"), ("diamond", "♦"), ("clubs", "♣")]
        return (Suit(name, symbol) for name, symbol in suits)

    def __create_deck(self):
        cards = []
        for suit in self.__create_suits():
            cards.append(Card("Ace", 1, suit))
            for i in range(2, 11):
                cards.append(Card(str(i), i, suit))
            cards.append(Card("Jack", 10, suit))
            cards.append(Card("Queen", 10, suit))
            cards.append(Card("King", 10, suit))

        random.shuffle(cards)
        return cards
    
    def shuffle_deck(self): 
        return random.shuffle(self.__cards)

    def get_next_card(self):
        return next(self.__card_iterator)

    def reset_deck(self):
        self.__cards = self.__create_deck()
        self.__card_iterator = iter(self.__cards)

    def get_cards(self):
        return self.__cards
