import random
from game.user import User
from object_value.gender import Gender
from object_value.level import Level
from player.bot import Bot

from ui.blackjack import Blackjack

BOTS = []

with open('bots.txt', 'r') as file:
        for line in file:
            name, gender = line.strip().split(',')
            BOTS.append((name, Gender[gender.strip().upper()]))

class Game:
    
    def __init__(self) -> None:
         self.players = []
            
    def create_bot(self, num_bots):
        level = random.choice(list(Level))  # Escolhe um nível aleatório para o bot
        balance = random.randrange(1000.00, 10001.00, 1000.00) # Saldo aleatório entre 1000 e 10000
        user = User(f"{BOTS[num_bots][0]} {BOTS[num_bots][1].symbol()} 🤖", level, BOTS[num_bots][0][1], round(balance,0))
        return Bot(user)


    def main(self):
        for j in range(8):
            player = self.create_bot(j)
            self.players.append(player)
            
        form = Blackjack(self.players)
        #form.start_game()
        form.run_game()

if __name__ == "__main__":
    game = Game()
    game.main()
