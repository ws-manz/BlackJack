import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.player import Player
from game.humanPlayer import HumanPlayer
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
                if isinstance(player, HumanPlayer):
                    print(f" {player.get_user().name} suas chances de blackjack são de {self.calculate_blackjack_probability(player)} %")
                if player.get_hand_value() >= 21:
                    break
                if player.play() == "hit":
                    self.__dealer.deal_card(player)
                else:
                    break

        # Dealer continua comprando cartas até atingir 17 pontos ou mais
        while self.__dealer.get_player().get_hand_value() < 17:
            self.__dealer.deal_card(self.__dealer.get_player())
    
    
    def calculate_blackjack_probability(self, player):
        remaining_cards = self.__dealer.remaining_cards()
        num_non_aces_and_tens = sum(1 for c in remaining_cards if c.value == 10)
        num_aces = sum(1 for c in remaining_cards if c.name == "Ace")

        # subtract the number of cards already in the player's hand from the count
        num_non_aces_and_tens -= len([c for c in player.get_hand() if c.value == 10])
        num_aces -= len([c for c in player.get_hand() if c.name == "Ace"])

        # calculate the probability of getting a blackjack
        if num_aces == 0:
            blackjack_prob = num_non_aces_and_tens / len(remaining_cards)
        else:
            non_aces_prob = num_non_aces_and_tens / len(remaining_cards)
            ace_prob = num_aces / len(remaining_cards)
            blackjack_prob = non_aces_prob * ace_prob * 2

        return round(blackjack_prob * 100, 2)
