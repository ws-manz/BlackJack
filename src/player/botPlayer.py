import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from object_value.level import Level
from typing import Any

class BotPlayer(Participant):
    def __init__(self, user) -> None:
        super().__init__(user)
        
    
    def play(self) -> str:
        #hand_value = self.get_hand_value()
        #level_min_value = Level(self.user.level).get_threshold()
        
        if self.hand.get_value() < self.get_user().level.value[1]:
            return 'hit'
        else:
            return 'stand'