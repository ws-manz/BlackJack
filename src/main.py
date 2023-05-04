from game.game import Game
from game.player import Player
from game.botPlayer import BotPlayer
from game.humanPlayer import HumanPlayer
from game.user import User
from game.level import Level

import random

BOT_NAMES = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Julia', 'Karen', 'Lucas', 'Maria', 'Nathan', 'Oliver', 'Pamela', 'Quentin', 'Rachel', 'Simon', 'Tina', 'Ursula', 'Victoria', 'Wendy', 'Xavier', 'Yvonne', 'Zara']

def main():
    # Cria um novo jogo
    game = Game()

    # Pergunta ao usuário quantos jogadores o jogo terá
    num_players = int(input("Quantos jogadores o jogo terá? "))
    max_players = 8 # Define o máximo de jogadores permitidos
    
    # Verifica se a quantidade de jogadores informada é válida
    if num_players <= 0 or num_players > max_players:
        print("Quantidade de jogadores inválida. O jogo terá 2 jogadores.")
        num_players = 1

    # Loop para adicionar os jogadores
    for i in range(num_players):
        # Pergunta os dados do jogador (nome, nível e dinheiro)
        name = input(f"Jogador {i+1}: Qual é o seu nome? ")
        level = input(f"Jogador {i+1}: Qual é o seu nível? (beginner, intermediate, advanced) ").lower()
        money = float(input(f"Jogador {i+1}: Informe seu saldo inicial: "))

        # Cria o usuário e o jogador com os dados informados
        user = User(name, Level[level.upper()], money)
        player = HumanPlayer(user)

        # Adiciona o jogador ao jogo
        game.add_player(player)

        num_bots = num_players - 1
        bot_names = BOT_NAMES[:num_bots]  # Seleciona os primeiros nomes da lista de bot_names

        # Pergunta se deseja adicionar mais jogadores
        if i+1 < num_players:
            add_player = input("Deseja adicionar mais jogadores? (Sim ou Não) ").lower()
            while add_player not in ["sim", "não"]:
                add_player = input("Deseja adicionar mais jogadores? (Sim ou Não) ").lower()

            if add_player == "não":
                # Adiciona bots para os jogadores restantes
                for j in range(i+1, num_players):
                    level = random.choice(list(Level))  # Escolhe um nível aleatório para o bot
                    balance = random.uniform(1000.00, 10000.00)  # Saldo aleatório entre 1000 e 10000
                    user = User(BOT_NAMES[j], level, balance)
                    player = BotPlayer(user)
                    game.add_player(player)
                break
    
    # Inicia o jogo
    # Inicia o jogo
    while True:
        game.start_game()
        answer = input("Deseja jogar novamente? (S/N) ")
        if answer.upper() != "S":
            break
    
    print("Fim de jogo.")

if __name__ == "__main__":
    main()