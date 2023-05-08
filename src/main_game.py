import random
from game.game import Game
from game.user import User
from object_value.gender import Gender
from object_value.level import Level
from player.bot import Bot

from ui.blackjack import Blackjack
from utils.console_logger import ConsoleLogger

BOTS = []

logger = ConsoleLogger()

with open('files/asserts/bots.txt', 'r') as file:
        for line in file:
            name, gender = line.strip().split(',')
            BOTS.append((name, Gender[gender.strip().upper()]))

class MyGame:
    
    def __init__(self) -> None:
         self.__game = Game()
            
    def create_bot(self, num_bots):
        level = random.choice(list(Level))  # Escolhe um nível aleatório para o bot
        balance = random.randrange(3000.00, 10001.00, 1000.00) # Saldo aleatório entre 1000 e 10000
        user = User(f"{BOTS[num_bots][0]} {BOTS[num_bots][1].symbol()} 🤖", name.lower(), level, BOTS[num_bots][1], round(balance,0))
        return Bot(user)


    def main(self):
        for j in range(8):
            player = self.create_bot(j)
            #self.players.append(player)
            self.__game.add_player(player)
        
        retorno = self.__game.start_game()
        logger.print_logs()
        
        form = Blackjack(self.__game.get_players())
        #form.start_game()
        form.run_game()

if __name__ == "__main__":
    game = MyGame()
    game.main()
