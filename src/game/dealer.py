import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.level import Level
from game.player import Player
from game.user import User

class Dealer:
    def __init__(self):
        self.__player = Player(User("Dealer", Level.ADVANCED, 100000))

    def get_player(self):
        return self.__player

