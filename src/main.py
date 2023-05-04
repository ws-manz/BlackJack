from game.game import Game
from game.player import Player
from game.user import User

def main():
    # Cria dois usuários, dois jogadores e adiciona eles no jogo
    u1 = User("Marco", 1000)
    u2 = User("Priscila",1000)
    p1 = Player(u1)
    p2 = Player(u2)
    
    # Cria um novo jogo
    game = Game()
    
    # Adiciona os jogadores ao jogo
    game.add_player(p1)
    game.add_player(p2)
    
    # Inicia o jogo
    game.start_game()

if __name__ == "__main__":
    main()