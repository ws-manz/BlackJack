import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.player import Player
from game.level import Level
from typing import Any

class HumanPlayer(Player):
    def __init__(self, user) -> None:
        super().__init__(user)
            
    def play(self) -> Any:
        while True:
            print(f"{self.get_user().name}: {[card.name + ' ' + card.suit.symbol for card in self.get_hand()]} - Points: {self.get_hand_value()}")
            
            response = input(f"{self.get_user().name}, do you want to hit or stand? ")
            if response.lower() == "hit":
                return "hit"
            elif response.lower() == "stand":
                return "stand"
            else:
                print("Invalid input. Please try again.")