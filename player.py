from card import Card
from user import User
from typing import Any
class Player:
    def __init__(self, user) -> None:
        self.__cards = []
        self.__user = user
    
    def add_card(self, card) -> Card:
        self.__cards.append(card)
    
    def get_user(self) -> User:
        return (self.__user)
      
    def get_cards(self):
        return (self.__cards)
        
    def show_cards(self):
        for card in self.__cards:
            print(f"{card.get_name()} {card.get_suit().get_name()}")
            
    def get_hand_value(self):
        hand_value = sum(card.get_value() for card in self.__cards)
        aces_count = sum(1 for card in self.__cards if card.get_name() == 'Ace')
        while hand_value > 21 and aces_count > 0:
            hand_value -= 10
            aces_count -= 1
        return hand_value