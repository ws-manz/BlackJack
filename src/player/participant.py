import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod

from object_value.level import Level
from object_value.handChoice import HandChoice
from game.user import User
from player.hand import Hand
from utils.base_class import BaseClass
from typing import Any

class Participant(BaseClass, ABC):

    HITS = ["Give me another card!","I'll take one more.","Hit me, dealer!"]
    STANDS = ["I'll stay with what I have.","I'm good, dealer. No more cards.","I'll stick with my hand."]
    SURRENDERS = ["I give up. Let's end this hand.","Fold. I surrender this round.","I forfeit. Time to start a new game."]

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
    
    def get_hands(self) -> list[Hand]:
        return (self.__hands)
    
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
        self.__hands[self.__current_hand_index].surrender = True
        return True
    
    def clear_hands(self):
        self.__hands[0].clear_cards()
        self.__hands[1].clear_cards()
        
    def get_hand_choice(self) -> HandChoice:
        has_cards_hand1 = self.__hands[0]
        has_cards_hand2 = self.__hands[1]
        
        if has_cards_hand1 and has_cards_hand2:
            return HandChoice.BOTH
        elif has_cards_hand1:
            return HandChoice.HAND1
        elif has_cards_hand2:
            return HandChoice.HAND2
        else:
            return HandChoice.NONE
        
    def meets_strip_condition(self) -> bool:
        if(self.get_user().level in [Level.INTERMEDIATE, Level.ADVANCED] and  len(self.hand) == 2 and 
                self.get_hand_choice() == HandChoice.HAND1):
            return  self.hand[0].value == self.hand[1].value
        else:
            return False