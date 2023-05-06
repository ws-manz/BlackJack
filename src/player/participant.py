import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod

from object_value.handChoice import HandChoice
from game.user import User
from player.Hand import Hand
from utils.base_class import BaseClass
from typing import Any

class Participant(BaseClass, ABC):
    def __init__(self, user: User) -> None:
        self.__user = user
        self.__hands = [Hand(), Hand()]  # lista contendo as duas mãos, inicialmente vazias
        self.__current_hand_index = 0  # índice da mão atual
        self.__surrender = False
        self.clear_hands() # limpar as mãos do jogador, para evitar que ao começar uma nova rodada já tenha cartas

    @property
    def hand(self):
        return self.__hands[self.__current_hand_index]
    
    def switch_hand(self, index: int):
        self.__current_hand_index = index
        
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
    
    def clear_hands(self):
        self.__hands[0].clear_cards()
        self.__hands[1].clear_cards()
        
    def get_hand_choice(self) -> HandChoice:
        has_cards_hand1 = bool(self.__hands[0].get_cards())
        has_cards_hand2 = bool(self.__hands[1].get_cards())
        
        if has_cards_hand1 and has_cards_hand2:
            return HandChoice.BOTH
        elif has_cards_hand1:
            return HandChoice.HAND1
        elif has_cards_hand2:
            return HandChoice.HAND2
        else:
            return HandChoice.NONE