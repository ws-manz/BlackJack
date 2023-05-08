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
    
    def distribute_cards(self):
        for player in self.__players:
            self.__dealer.deal_card(player)  # Distribui uma carta para cada jogador
        self.__dealer.deal_dealer_card() # Distribui uma carta para o dealer
        self.show_cards() # Mostra as cartas dos jogadores e do dealer
    
    def distribute_cards_dealer(self):
        # Dealer continua comprando cartas até atingir 17 pontos ou mais
        while self.__dealer.my_hand_value() < 17:
            self.__dealer.deal_card(self.__dealer.get_player())
            
    def __deal_additional_cards(self, player:Participant):
                   
        current_hand_index = 0
        for my_hand in player.get_hands():   

            if(not my_hand.has_cards()):
                break

            player.switch_hand(current_hand_index)     
            current_hand_index =1    
            while True:                                          
                
                if player.meets_strip_condition():
                    self.strip(player)

                if isinstance(player, Player):
                    self.logger.log(f"### {player.get_user().name} your chances of blackjack are {self.calculate_blackjack_probability(player)}% ###")
                    
                if player.hand.get_value() >= 21:
                    break
                
                if isinstance(player, Bot):
                    if player.hand.get_value() >= 13 and player.hand.get_value() <= 14 and (self.__dealer.get_player().hand.get_cards()[0].value == 1):
                        player.wants_to_surrender()
                        break
                
                if player.wants_to_hit():
                    if player.hand.surrender: #  player.surrender:
                        break                            
                    self.__dealer.deal_card(player)
                else:
                    break                
        # Observação: Se jogador não ultrapassou 21 pontos ou não decidiu parar de comprar cartas, continue distribuindo mais cartas
        current_hand_index = 0
    
    def strip(self, player):
        #self.logger.log("Player's first card is a 10!")
        if isinstance(player, Player):
            response = input("Do you want to strip? (Sim/Não): ")
            if response.lower() in ["sim", "s"]:
                player.switch_hand(1)
                self.__dealer.deal_card(player)
                player.switch_hand(0)
        elif(isinstance(player, Bot)):
            player.switch_hand(1)
            self.__dealer.deal_card(player)
            player.switch_hand(0)
                                 
    def deal_cards(self):
        self.distribute_cards()
        
        # Distribui mais cartas para cada jogador até que ele tenha atingido o valor mínimo para o nível dele ou tenha ultrapassado 21 pontos
        for player in self.__players:
            self.__deal_additional_cards(player)
        
        self.distribute_cards_dealer()
        
        
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
