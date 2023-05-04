from game.game import Game
from game.player import Player
from game.user import User
from game.level import Level

def main():
    # Cria dois usuários, dois jogadores e adiciona eles no jogo
    p1 = Player(User("Marco", Level.BEGINNER, 1000.00))
    p2 = Player(User("Priscila", Level.INTERMEDIATE, 2000.00))
    p3 = Player(User("Duda", Level.ADVANCED, 5000.00))
    
    # Cria um novo jogo
    game = Game()
    
    # Adiciona os jogadores ao jogo
    game.add_player(p1)
    game.add_player(p2)
    game.add_player(p3)
    
    # Inicia o jogo
    game.start_game()

if __name__ == "__main__":
    main()