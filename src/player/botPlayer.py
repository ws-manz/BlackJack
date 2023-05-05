import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from typing import Any

class BotPlayer(Participant):
    def __init__(self, user) -> None:
        super().__init__(user)
            
    def wants_to_hit(self) -> bool:        
        return self.hand.get_value() < self.get_user().level.value[1]