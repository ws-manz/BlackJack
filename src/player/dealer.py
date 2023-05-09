import os
import sys
from object_value.gender import Gender
from object_value.result import Result

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from object_value.level import Level
from player.bot import Bot
from player.participant import Participant
from game.user import User
from utils.base_class import BaseClass

class Dealer(BaseClass):
    def __init__(self, deck = []):
        player = User("Dealer 🎰", "dealer" , Level.ADVANCED, Gender.MALE,  1000000.00)
        self.__player = Bot(player)
        self.__deck = deck
        
    def get_player(self):
        return self.__player
    
    def reset_deck(self):
        self.__deck.reset_deck()
        self.__player.hand.clear_cards()
    
    def deal_card(self, player : Participant):
        # Distribui uma carta para o jogador
        player.hand.add_card(self.__deck.get_next_card())
    
    def deal_dealer_card(self):
        # Distribui uma carta para o dealer
        self.__player.hand.add_card(self.__deck.get_next_card())
    
    def my_hand_value(self)        :
        return self.__player.hand.get_value()
    
    def remaining_cards(self):
        return self.__deck.get_cards()

