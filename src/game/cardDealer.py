import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from player.player import Player
from player.bot import Bot
from player.dealer import Dealer
from utils.utils import Utils
from object_value.level import Level
from object_value.handChoice import HandChoice
from utils.base_class import BaseClass

class CardDealer(BaseClass):
    def __init__(self, players: List[Participant], dealer: Dealer, bet:float):
        self.__players = [player for player in players if player.get_user().can_afford_bet(bet)]

        self.__dealer = dealer
        
    def deal_cards(self):
        for player in self.__players:
            self.__dealer.deal_card(player)  # Distribui uma carta para cada jogador

        self.__dealer.deal_card(self.__dealer.get_player()) # Distribui uma carta para o dealer

        self.show_cards() # Mostra as cartas dos jogadores e do dealer
        
        # Distribui mais cartas para cada jogador até que ele tenha atingido o valor mínimo para o nível dele ou tenha ultrapassado 21 pontos
        for player in self.__players:
            while True:
                if isinstance(player, Player):
                    self.logger.log(f"### {player.get_user().name} your chances of blackjack are {self.calculate_blackjack_probability(player)}% ###")
                if player.hand.get_value() >= 21:
                    break
                
                if isinstance(player, Bot):
                    if player.hand.get_value() >= 13 and player.hand.get_value() <= 14 and (self.__dealer.get_player().hand.get_cards()[0].value == 1):
                        player.wants_to_surrender()
                        break
                
                if (player.level == Level.INTERMEDIATE or player.level == Level.ADVANCED) and len(player.hand.get_cards()) == 1 and player.hand.get_cards()[0].value == 10 and player.get_hand_choice() == HandChoice.HAND1:
                    self.logger.log("Player's first card is a 10!")
                        
                if player.wants_to_hit():
                    if player.surrender:
                        break                            
                    self.__dealer.deal_card(player)
                else:
                    break                
                # Observação: Se jogador não ultrapassou 21 pontos ou não decidiu parar de comprar cartas, continue distribuindo mais cartas

        # Dealer continua comprando cartas até atingir 17 pontos ou mais
        while self.__dealer.get_player().hand.get_value() < 17:
            self.__dealer.deal_card(self.__dealer.get_player())
        
    def calculate_blackjack_probability(self, player:Participant):
        remaining_cards = self.__dealer.remaining_cards()
        blackjack_prob = Utils.calculate_blackjack_probability(remaining_cards, player.hand.get_cards())

        return blackjack_prob
    
    def show_cards(self):
        # Mostra a primeira carta de cada jogador e do dealer
        self.logger.log("### Dealer ###")
        self.logger.log(f"Dealer's card: {[card.name + ' ' + card.suit.symbol for card in self.__dealer.get_player().hand.get_cards()]}")

        for player in self.__players:
            self.logger.log(f"### {player.get_user().name} ###")
            
            cards = player.hand.get_cards()
            self.logger.log(f"Player's card: {[card.name + ' ' + card.suit.symbol for card in cards]}")
