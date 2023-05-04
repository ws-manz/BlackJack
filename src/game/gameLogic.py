import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.player import Player
from game.level import Level
from game.dealer import Dealer

class GameLogic:
    def __init__(self, players: List[Player], dealer: Dealer):
        self.players = players
        self.dealer = dealer

    def determine_winners(self):
        winners = []
        dealer_value = self.dealer.get_player().get_hand_value()
        for player in self.players:
            if player.get_hand_value() <= 21 and (dealer_value > 21 or player.get_hand_value() > dealer_value):
                winners.append(player)
        return winners