import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from object_value.level import Level
from player.dealer import Dealer
from utils.base_class import BaseClass

class GameLogic(BaseClass):
    def __init__(self, players: List[Participant], dealer: Dealer):
        self.players = players
        self.dealer = dealer  
    
    def get_winners(self):
        winners = []
        dealer_value = self.dealer.get_player().hand.get_value()
        for player in self.players:
            player_value = player.hand.get_value()
            """
            Retorna uma lista com os jogadores que ganharam a rodada.

            Para um jogador ganhar, é necessário:
            - O valor total da mão do jogador não pode ultrapassar 21 pontos.
            - Se o valor total da mão do dealer ultrapassar 21 pontos ou o valor total da mão do jogador for maior do que o do dealer, o jogador vence.
            - Se o jogador tiver exatamente duas cartas na mão e o valor total for 21, então ele fez um blackjack e vence, a menos que o dealer também tenha feito um blackjack.
            """
            is_blackjack = player_value == 21 and len(player.hand.get_cards()) == 2
            if player_value <= 21 and (dealer_value > 21 or player_value > dealer_value or is_blackjack and dealer_value != 21):
                winners.append(player)
        return winners