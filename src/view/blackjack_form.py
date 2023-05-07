import pygame
import sys


class BlackjackForm:
    def __init__(self, players):
        # Inicializa o Pygame
        pygame.init()

        # Define o tamanho da janela
        self.WINDOW_WIDTH = 1024
        self.WINDOW_HEIGHT = 768

        # Cria uma nova janela
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # Define o título da janela
        pygame.display.set_caption('Blackjack')

        # Define a cor da mesa de blackjack e o fundo da tela
        self.BLACKJACK_TABLE_COLOR = (0, 128, 0)  # verde escuro
        self.TABLE_BORDER_COLOR = (0, 0, 0)  # preto
        self.BACKGROUND_COLOR = (0, 100, 0)  # verde mais claro
        self.screen.fill(self.BACKGROUND_COLOR)

        self.FONT_CARD_PATH = 'fonts/arial-unicode-ms.ttf'
        self.FONT_TITLE_PATH = 'fonts/blackjackregular.ttf'
        self.FONT_PATH = 'fonts/arial-unicode-ms.ttf'
        self.FONT_NAME_PATH = 'fonts/montserrat.otf'

        self.players = players

        # Define a fonte e o tamanho do texto do título
        self.title_font = pygame.font.Font(self.FONT_TITLE_PATH, 80)
        self.title_text = self.title_font.render("BlackJack em Python", True, (255, 255, 255))

        self.hand_dealer_rects = []
        self.hand_player_rects = []


    def draw_title(self):
        # Obtém a posição central do texto do título
        title_rect = self.title_text.get_rect(center=(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))

        # Desenha o texto do título em negrito no meio da tela
        pygame.draw.rect(self.screen, self.BACKGROUND_COLOR, title_rect)
        self.screen.blit(self.title_text, title_rect)

    def draw_dealer(self):
        # Desenha o espaço para o dealer
        dealer_rect = pygame.Rect(450, 80, 100, 100)
        pygame.draw.rect(self.screen, self.TABLE_BORDER_COLOR, dealer_rect, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), dealer_rect, 2)

        # Desenha os espaços para as cartas da mão do dealer
        self.hand_dealer_rects = []
        num_cards = 10
        #total_hand_width = (40 + 5) * num_cards - 5
        #x_offset = (self.WINDOW_WIDTH - total_hand_width) // 2
        x_offset = 280
        y_offset = dealer_rect.top + dealer_rect.height + 20

        for i in range(num_cards):
            hand_rect = pygame.Rect(x_offset + i * (40 + 5), y_offset, 40, 50)
            self.hand_dealer_rects.append(hand_rect)
            pygame.draw.rect(self.screen, self.TABLE_BORDER_COLOR, hand_rect, 2)


        self.draw_deck()


    def draw_deck(self):
        # Desenha o retângulo para o baralho
        deck_rect = pygame.Rect(570, 130, 40, 50)
        pygame.draw.rect(self.screen, self.TABLE_BORDER_COLOR, deck_rect, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), deck_rect, 2)

    def draw_players(self):
        # Define o tamanho e espaçamento dos retângulos dos jogadores
        player_rect_width = 100
        player_rect_height = 100
        player_rect_spacing = 20

        # Posiciona os jogadores no centro da tela, abaixo da mesa
        player_rects = []
        total_player_width = (player_rect_width + player_rect_spacing) * 8 - player_rect_spacing
        x_offset = (self.WINDOW_WIDTH - total_player_width) // 2
        y_offset = self.WINDOW_HEIGHT - player_rect_height - 50

        self.hand_player_rects = []
        for i in range(8):
            player_rect = pygame.Rect(x_offset + i * (player_rect_width + player_rect_spacing), y_offset,
                                    player_rect_width, player_rect_height)
            player_rects.append(player_rect)

            # Desenha o retângulo do jogador
            pygame.draw.rect(self.screen, self.BLACKJACK_TABLE_COLOR, player_rect)
            pygame.draw.rect(self.screen, self.TABLE_BORDER_COLOR, player_rect, 2)

            # Desenha o nome do jogador abaixo do espaço
            font = pygame.font.Font(self.FONT_NAME_PATH, 16)
            text = font.render(self.players[i], True, (255, 255, 255))
            text_rect = text.get_rect(center=player_rect.center)
            text_rect.top = player_rect.bottom + 5
            self.screen.blit(text, text_rect)

            # Desenha os espaços para as cartas do jogador
            card_rect_width = 40
            card_rect_height = 50
            card_rect_spacing = 10
            card_rect1 = pygame.Rect(player_rect.left + 10, player_rect.top - card_rect_height - card_rect_spacing,
                                    card_rect_width, card_rect_height)
            card_rect2 = pygame.Rect(player_rect.left + 10 + card_rect_width + card_rect_spacing, player_rect.top - card_rect_height - card_rect_spacing,
                                    card_rect_width, card_rect_height)

            pygame.draw.rect(self.screen, (255, 255, 255), card_rect1, 2)
            pygame.draw.rect(self.screen, (255, 255, 255), card_rect2, 2)

            self.hand_player_rects.append( [card_rect1, card_rect2])

    def draw_card(self, x, y, value, suit):
        # Define o tamanho da carta
        card_width = 30
        card_height = 40

        # Define as cores da carta
        card_color = (255, 255, 255)
        symbol_color = (0, 0, 0)

        # Define as posições dos elementos na carta
        center_pos = (x + card_width // 2, y + card_height // 2)
        bottom_left_pos = (x+2, y + card_height)

        # Define a cor da fonte com base no naipe da carta
        if suit in ["Hearts", "Diamonds", "♥", "♦"]:
            symbol_color = (255, 0, 0)

        # Desenha o retângulo da carta
        card_rect = pygame.Rect(x, y, card_width, card_height)
        pygame.draw.rect(self.screen, card_color, card_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), card_rect, 1)

        # Desenha o número e símbolo no centro da carta
        center_font = pygame.font.Font(self.FONT_CARD_PATH, 15)
        center_text = center_font.render(str(value) + suit, True, symbol_color)
        center_text_rect = center_text.get_rect(center=center_pos)
        self.screen.blit(center_text, center_text_rect)

        # Desenha o texto abaixo e alinhado à esquerda
        bottom_left_font = pygame.font.Font(self.FONT_CARD_PATH, 8)
        bottom_left_text = bottom_left_font.render(str(value) + suit, True,symbol_color)
        bottom_left_text_rect = bottom_left_text.get_rect(bottomleft=bottom_left_pos)
        self.screen.blit(bottom_left_text, bottom_left_text_rect)


    def draw_blackjack_table(self):
        self.draw_dealer()
        self.draw_players()

        for rect in self.hand_dealer_rects:
            self.draw_card(rect.x+5, rect.y+5, 7, '♣')

            for rect in self.hand_player_rects:
                rect0 = rect[0]
                rect1 = rect[1]
                self.draw_card(rect0.x+5, rect0.y+5, 7, '♥')
                self.draw_card(rect1.x+5, rect1.y+5, 'K', '♣')

                self.draw_card(rect0.x+10, rect0.y-5, 10, '♣')
                self.draw_card(rect0.x+20, rect0.y-15, 10, '♥')
                self.draw_card(rect0.x+30, rect0.y-25, 10, '♣')

                self.draw_card(rect1.x+10, rect1.y-5, 10, '♣')
                self.draw_card(rect1.x+20, rect1.y-15, 10, '♥')
                self.draw_card(rect1.x+30, rect1.y-25, 10, '♣')

            self.draw_card(575, 135, 'A', '♣')

        # Atualiza a tela
        pygame.display.flip()


    def run_game(self):
        # Loop principal do jogo
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_title()
            self.draw_blackjack_table()