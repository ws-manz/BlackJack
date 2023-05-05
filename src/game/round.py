import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from object_value.result import Result
from player.dealer import Dealer
from game.gameLogic import GameLogic
from game.cardDealer import CardDealer
from game.gameView import GameView


class Round:
    def __init__(self, players: list[Participant], dealer: Dealer, bet: float = 100.00) -> None:
        self.__players = players
        self.__dealer = dealer
        self.__bet = bet
        self.__game_logic = GameLogic(self.__players,  self.__dealer)
        self.__card_dealer = CardDealer(self.__players, self.__dealer, self.__bet)
        self.__game_view = GameView(self.__players, self.__dealer)

    def play(self):
        # Distribui uma carta para cada jogador e para o dealer
        self.__card_dealer.deal_cards()

        # Verifica o vencedor do jogo
        winners = self.__game_logic.get_winners()
                
         # Exibe as cartas de cada jogador e do dealer
        print("\nPlayers' cards and points:")
        for player in self.__players:
            self.__game_view.display_player_cards(player)
        
        self.__game_view.display_dealer_cards()

        if len(winners) == 0:
            print("\nDealer wins! All players lost.")
            for player in self.__players:
                player.get_user().update_balance(Result.LOSS, self.__bet) 
        else:
            for player in self.__players:
                if player in winners:
                    player.get_user().update_balance(Result.WIN, self.__bet) # bonifica os vencedores com o dobro da aposta
                else:
                    player.get_user().update_balance(Result.LOSS, self.__bet) # penaliza os perdedores com o valor da aposta

        self.__game_view.display_round_result(winners)    

        
                
