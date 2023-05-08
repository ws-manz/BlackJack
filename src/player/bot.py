import os
import sys
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from typing import Any

class Bot(Participant):
    def __init__(self, user) -> None:
        super().__init__(user)
            
    def wants_to_hit(self) -> bool:   

        is_hit = self.hand.get_value() < self.get_user().level.value[1]        
        if(is_hit):
            self.logger.log(f"{self.get_user().name} says: {random.choice(super().HITS)}") 
        else:
            self.logger.log(f"{self.get_user().name} says: {random.choice(super().STANDS)}") 
        return is_hit