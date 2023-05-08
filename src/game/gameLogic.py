import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from object_value.level import Level
from object_value.handChoice import HandChoice 
from player.hand import Hand
from player.dealer import Dealer
from utils.base_class import BaseClass

class GameLogic(BaseClass):
    def __init__(self, players: List[Participant], dealer: Dealer):
        self.players = players
        self.dealer = dealer  
    
    def get_winners(self):
        winners = []
        dealer_value = self.dealer.get_player().hand.get_value()
        hands_won = 0
        for player in self.players:
            
            if(player.get_hand_choice() == HandChoice.HAND1):
                if self.has_winner(dealer_value, player.hand):
                    hands_won += 1
                    player.hand.win = True
            
            if(player.get_hand_choice() == HandChoice.BOTH):
                for i in range(0, 2):                    
                    player.switch_hand(i)
                    if self.has_winner(dealer_value, player.hand):
                        hands_won += 1
                        player.hand.win = True                  
                player.switch_hand(0)
            if hands_won > 0:
                winners.append((player, hands_won))
                
            hands_won = 0
        return winners
    
    def has_winner(self, dealer_value, hand:Hand) -> bool:        
            player_value = hand.get_value()
            """
            Retorna uma lista com os jogadores que ganharam a rodada.

            Para um jogador ganhar, é necessário:
            - O valor total da mão do jogador não pode ultrapassar 21 pontos.
            - Se o valor total da mão do dealer ultrapassar 21 pontos ou o valor total da mão do jogador for maior do que o do dealer, o jogador vence.
            - Se o jogador tiver exatamente duas cartas na mão e o valor total for 21, então ele fez um blackjack e vence, a menos que o dealer também tenha feito um blackjack.
            """
            is_blackjack = hand.is_blackjack() and len(hand.get_cards()) == 2
            return player_value <= 21 and (dealer_value > 21 or player_value > dealer_value or is_blackjack and dealer_value != 21)
                