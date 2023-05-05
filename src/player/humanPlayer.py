import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from object_value.level import Level
from typing import Any

class HumanPlayer(Participant):
    def __init__(self, user) -> None:
        super().__init__(user)
            
    def play(self) -> str:
        while True:
            print(f"{self.get_user().name}: {[card.name + ' ' + card.suit.symbol for card in self.get_hand()]} - Points: {self.calculate_hand_value()}")
            
            response = input(f"{self.get_user().name}, do you want to hit or stand? ")
            if response.lower() == "hit":
                return "hit"
            elif response.lower() == "stand":
                return "stand"
            else:
                self.logger.log("Invalid input. Please try again.")