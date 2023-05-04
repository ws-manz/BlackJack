import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.player import Player
from game.level import Level
from game.dealer import Dealer


class Round:
    def __init__(self, players: list[Player], dealer: Dealer) -> None:
        self.__players = players
        self.__dealer = dealer

    def play(self):
        # Distribui uma carta para cada jogador e para o dealer
        for player in self.__players:
            self.__dealer.deal_card(player)
        self.__dealer.deal_card(self.__dealer.get_player())

        # Define o valor mínimo de pontos para parar de receber cartas, de acordo com o nível do jogador
        level_min_values = {Level.BEGINNER: 17, Level.INTERMEDIATE: 18, Level.ADVANCED: 19}

        # Distribui mais cartas para cada jogador até que ele tenha atingido o valor mínimo para o nível dele ou tenha ultrapassado 21 pontos
        for player in self.__players:
            while True:
                if player.get_hand_value() >= 21:
                    break
                if player.get_hand_value() < level_min_values[player.get_user().level]:
                    self.__dealer.deal_card(player)
                else:
                    break

        # Dealer continua comprando cartas até atingir 17 pontos ou mais
        while self.__dealer.get_player().get_hand_value() < 17:
            self.__dealer.deal_card(self.__dealer.get_player())

        # Verifica o vencedor do jogo
        winners = []
        dealer_value = self.__dealer.get_player().get_hand_value()
        for player in self.__players:
            if player.get_hand_value() <= 21 and (dealer_value > 21 or player.get_hand_value() > dealer_value):
                winners.append(player)
        if len(winners) == 0:
            print("\nDealer wins! All players lost.")
        else:
            print("\nWinners:")
            for winner in winners:
                print(f"{winner.get_user().name} - {winner.get_hand_value()} points")
