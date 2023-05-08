import os
import sys
from game.playerManager import PlayerManager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from object_value.result import Result
from player.dealer import Dealer
from game.gameLogic import GameLogic
from game.cardDealer import CardDealer
from game.gameView import GameView
from utils.base_class import BaseClass

class Round(BaseClass):
    def __init__(self, players: list[Participant], dealer: Dealer, bet: float = 1000.00) -> None:
        self.__players = players               
        self.__dealer = dealer
        self.__bet = bet
        
        self.__players = self.update_active_players()
        self.__game_logic = GameLogic(self.__players,  self.__dealer)
        self.__card_dealer = CardDealer(self.__players, self.__dealer, self.__bet)
        self.__game_view = GameView(self.__players, self.__dealer)
        self.__player_manager = PlayerManager(bet)
    
    def update_active_players(self):
        return [player for player in self.__players if player.get_user().can_afford_bet(self.__bet)]
    
    def clear_surrender_players(self):
        for player in self.__players:
            player.surrender = False
    
    def play(self):
        self.clear_surrender_players()
        
        self.__game_view.display_players_balance()
        
        # Distribui uma carta para cada jogador e para o dealer
        self.__card_dealer.deal_cards()   
             
        # Verifica o vencedor do jogo
        winners = self.__game_logic.get_winners()
        winning_players = []
        
        for winner in winners:
            winning_players.append(winner[0])
                
         # Exibe as cartas de cada jogador e do dealer
        self.logger.log("\n#### Players' cards and points ####")
        for player in self.__players:
            self.__game_view.display_player_cards(player)
        
        self.logger.log("\n#### Dealer cards and points ####")
        self.__game_view.display_dealer_cards()

        # Atualiza o saldo dos jogadores
        self.__player_manager.update_balances(self.__players, winners)
        
        
                                            
        self.__game_view.display_round_result(winning_players)
        
                
