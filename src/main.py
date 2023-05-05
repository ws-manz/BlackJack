from game.game import Game
from player.botPlayer import BotPlayer
from player.humanPlayer import HumanPlayer
from game.user import User
from object_value.level import Level
from utils.console_logger import ConsoleLogger

import random

BOT_NAMES = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Julia', 'Karen', 'Lucas', 'Maria', 'Nathan', 'Oliver', 'Pamela', 'Quentin', 'Rachel', 'Simon', 'Tina', 'Ursula', 'Victoria', 'Wendy', 'Xavier', 'Yvonne', 'Zara']
logger = ConsoleLogger()

def create_player(player_num):
    # Pergunta os dados do jogador (nome, nível e dinheiro)
    name = input(f"Jogador {player_num}: Qual é o seu nome? ")
    level = input(f"Jogador {player_num}: Qual é o seu nível? (beginner, intermediate, advanced) ").lower()
    money = float(input(f"Jogador {player_num}: Informe seu saldo inicial: "))

    # Cria o usuário e o jogador com os dados informados
    user = User(name, Level[level.upper()], money)
    player = HumanPlayer(user)

    return player

def create_bot(num_bots):
    level = random.choice(list(Level))  # Escolhe um nível aleatório para o bot
    balance = random.uniform(1000.00, 10000.00)  # Saldo aleatório entre 1000 e 10000
    user = User(BOT_NAMES[num_bots], level, balance)
    player = BotPlayer(user)

    return player

def main():
    # Cria um novo jogo
    game = Game()

    # Pergunta ao usuário quantos jogadores o jogo terá
    num_players = int(input("Quantos jogadores o jogo terá? "))
    max_players = 8 # Define o máximo de jogadores permitidos
    
    # Verifica se a quantidade de jogadores informada é válida
    if num_players <= 0 or num_players > max_players:
        print("Quantidade de jogadores inválida. O jogo terá 2 jogadores.")
        num_players = 2

    # Adiciona o jogador humano
    player_num = 1
    player = create_player(player_num)
    game.add_player(player)

    # Loop para adicionar os jogadores bots
    for i in range(num_players-1):
        add_player = input("Deseja adicionar mais jogadores? (Sim ou Não) ").lower()
        while add_player not in ["sim", "não"]:
            add_player = input("Deseja adicionar mais jogadores? (Sim ou Não) ").lower()

        if add_player == "não":
            num_bots = num_players - i - 1
            for j in range(num_bots):
                player = create_bot(j)
                game.add_player(player)
            break

        player_num += 1
        player = create_player(player_num)
        game.add_player(player)

    # Inicia o jogo
    while True:
        game.start_game()
        logger.print_logs()
        answer = input("Deseja jogar novamente? (S/N) ")
        if answer.upper() != "S":
            break

    print("Fim de jogo.")

if __name__ == "__main__":
    main()