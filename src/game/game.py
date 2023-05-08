import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from player.dealer import Dealer  # importa a classe Dealer
from card.deck import Deck 
from game.round import Round # importa a classe Round
from utils.base_class import BaseClass

from abc import ABC, abstractmethod

class GameObserver(ABC):
    @abstractmethod
    def start_game(self):
        pass

class GameInputHandler(ABC):
    @abstractmethod
    def add_player(self, player: Participant) -> Participant:
        pass
    
class Game(BaseClass):
    #    def __init__(self, players: List[Player], dealer: Dealer, input_handler: GameInputHandler, observer: GameObserver) -> None:
    def __init__(self, max_players: int = 8, min_players: int = 1) -> None:
        self.__players = []
        self.__dealer = Dealer(Deck())    
        self.__max_players = max_players
        self.__min_players = min_players
    
    @property
    def max_players(self) -> int:
        return self.__max_players
    
    def is_valid_player_count(self):
        return self.__min_players <= len(self.__players) <= self.__max_players
    
    def reset_game(self):    
        self.logger.log("Shuffled deck")
        self.__dealer.reset_deck()
        for player in self.__players:
            player.clear_hands()
        
    def add_player(self, player : Participant) -> bool :
        if len(self.__players) >= self.__max_players:
            self.logger.log("Maximum number of players reached.")
            return False
        self.__players.append(player)
        return True

    def get_players(self) -> list[Participant]: 
        return self.__players
        
    def start_game(self) -> bool:
        # Reinicia o jogo
        self.reset_game()
        
        # Verifica se há pelo menos um jogador no jogo
        if len(self.__players) == 0 :
            self.logger.log("*Insufficient number of players*")
            return False
        
        self.logger.log("*Game started, Welcome!*")
        
        # Inicia a rodada
        self.play_round()
        return True
    
    def play_round(self):
        round = Round(self.__players, self.__dealer) # cria o objeto Round
        round.play() # chama o método play() da classe Round para iniciar a rodada
        self.__players = round.update_active_players()
