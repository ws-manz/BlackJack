import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from player.humanPlayer import HumanPlayer
from player.dealer import Dealer
from utils.utils import Utils
from utils.base_class import BaseClass

class CardDealer(BaseClass):
    def __init__(self, players: List[Participant], dealer: Dealer, bet:float):
        self.__players = players
        self.__dealer = dealer
        self.__bet = bet

    def deal_cards(self):
        for player in self.__players:
            if not player.get_user().can_afford_bet(self.__bet): # verifica se o saldo é suficiente para a aposta
                self.__players.remove(player) # remove o jogador da lista de jogadores
                continue                    
            self.__dealer.deal_card(player)

        self.__dealer.deal_card(self.__dealer.get_player())

        # Distribui mais cartas para cada jogador até que ele tenha atingido o valor mínimo para o nível dele ou tenha ultrapassado 21 pontos
        for player in self.__players:
            while True:
                if isinstance(player, HumanPlayer):
                    self.logger.log(f"### {player.get_user().name} suas chances de blackjack são de {self.calculate_blackjack_probability(player)}% ###")
                if player.hand.get_value() >= 21:
                    break
                if player.play() == "hit":
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
