import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from player.player import Player
from player.bot import Bot
from player.dealer import Dealer
from utils.utils import Utils
from utils.base_class import BaseClass

class CardDealer(BaseClass):
    def __init__(self, players: List[Participant], dealer: Dealer, bet:float):
        self.__players = [player for player in players if player.get_user().can_afford_bet(bet)]

        self.__dealer = dealer
        
    def deal_cards(self):
        for player in self.__players:
            self.__dealer.deal_card(player)

        self.__dealer.deal_card(self.__dealer.get_player())

        # Distribui mais cartas para cada jogador até que ele tenha atingido o valor mínimo para o nível dele ou tenha ultrapassado 21 pontos
        for player in self.__players:
            while True:
                if isinstance(player, Player):
                    self.logger.log(f"### {player.get_user().name} suas chances de blackjack são de {self.calculate_blackjack_probability(player)}% ###")
                if player.hand.get_value() >= 21:
                    break
                
                if isinstance(player, Bot):
                    if player.hand.get_value() >= 13 and player.hand.get_value() <= 14 and (self.__dealer.get_player().hand.get_cards()[0].value == 1 or self.__dealer.get_player().hand.get_cards()[0].value == 10):
                        player.wants_to_surrender()
                        break
                    
                if player.wants_to_hit():
                    self.__dealer.deal_card(player)
                else:
                    break

        # Dealer continua comprando cartas até atingir 17 pontos ou mais
        while self.__dealer.get_player().hand.get_value() < 17:
            self.__dealer.deal_card(self.__dealer.get_player())
    
    
    def calculate_blackjack_probability(self, player:Participant):
        remaining_cards = self.__dealer.remaining_cards()
        blackjack_prob = Utils.calculate_blackjack_probability(remaining_cards, player.hand.get_cards())

        return blackjack_prob
