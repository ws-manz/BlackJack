import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.player import Player
from game.level import Level
from game.dealer import Dealer


class CardDealer:
    def __init__(self, players: List[Player], dealer: Dealer, bet:float):
        self.__players = players
        self.__dealer = dealer
        self.__bet = bet

    def deal_cards(self):
        for player in self.__players:
            if player.get_user().balance < self.__bet: # verifica se o saldo é suficiente para a aposta
                self.__players.remove(player) # remove o jogador da lista de jogadores
                continue
            self.__dealer.deal_card(player)

        self.__dealer.deal_card(self.__dealer.get_player())

        # Distribui mais cartas para cada jogador até que ele tenha atingido o valor mínimo para o nível dele ou tenha ultrapassado 21 pontos
        for player in self.__players:
            while True:
                if player.get_hand_value() >= 21:
                    break
                if player.play() == "hit":
                    self.__dealer.deal_card(player)
                else:
                    break

        # Dealer continua comprando cartas até atingir 17 pontos ou mais
        while self.__dealer.get_player().get_hand_value() < 17:
            self.__dealer.deal_card(self.__dealer.get_player())