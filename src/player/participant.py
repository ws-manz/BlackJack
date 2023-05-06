import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod

from card.card import Card
from game.user import User
from player.Hand import Hand
from utils.base_class import BaseClass
from typing import Any

class Participant(BaseClass, ABC):
    def __init__(self, user: User) -> None:
        self.__user = user
        self.__hand = Hand()
        #self.__hands = [Hand(), Hand()]  # lista contendo as duas mãos, inicialmente vazias
        self.__hand.clear_cards()
        self.__surrender = False

    @property
    def hand(self):
        return self.__hand
    
    def get_user(self) -> User:
        return self.__user
    
    @property
    def surrender(self):
        return self.__surrender
    
    @surrender.setter
    def surrender(self, surrender: bool):
        self.__surrender = surrender
    
    @abstractmethod  
    def wants_to_hit(self) -> bool:
        pass
       
    def wants_to_surrender(self) -> bool:
        self.logger.log(f"{self.get_user().name} chose to surrender. Quit the game.")
        self.__surrender = True
        return True