import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from card.card import Card
from game.user import User
from typing import Any

class Player:
    def __init__(self, user) -> None:
        self.__cards = []
        self.__user = user
    
    def add_card(self, card) -> Card:
        self.__cards.append(card)
    
    def get_user(self) -> User:
        return (self.__user)
      
    def get_hand(self):
        return (self.__cards)
        
    def show_cards(self):
        for card in self.__cards:
            print(f"{card.name} {card.suit.name}")
            
    def get_hand_value(self):
        hand_value = sum(card.value for card in self.__cards)
        aces_count = sum(1 for card in self.__cards if card.name == 'Ace')
        while hand_value > 21 and aces_count > 0:
            hand_value -= 10
            aces_count -= 1
        return hand_value