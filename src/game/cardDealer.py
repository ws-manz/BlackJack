import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.player import Player
from game.level import Level
from game.dealer import Dealer


class CardDealer:
    def __init__(self, players: List[Player], dealer: Dealer, bet:float):
        self.players = players
        self.dealer = dealer
        self.__bet = bet

    def deal_cards(self):
        for player in self.players:
            if player.get_user().balance < self.__bet:
            #if player.get_balance() < player.get_bet():
                self.players.remove(player)
                continue
            self.dealer.deal_card(player)

        self.dealer.deal_card(self.dealer.get_player())

        while True:
            players_in_game = [player for player in self.players if player.get_hand_value() < 21]
            if not players_in_game:
                break
            for player in players_in_game:
                if player.play() == "hit":
                    self.dealer.deal_card(player)
                else:
                    break

        while self.dealer.get_player().get_hand_value() < 17:
            self.dealer.deal_card(self.dealer.get_player())