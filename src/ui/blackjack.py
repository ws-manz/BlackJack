import pygame
import sys
import pygame.time

from object_value.result import Result
from ui.HandPlayerRect import HandPlayerRect

class Blackjack:
    
    # Define o tamanho da janela
    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 768
    
     # Dimensões dos elementos da interface
    CARD_RECT_WIDTH = 40
    CARD_RECT_HEIGHT = 50
    PLAYER_HAND_WIDTH = 100
    PLAYER_HAND_HEIGHT = 100
    PLAYER_HAND_SPACING = 20
    
    COLOR_FONT_DEFAULT = (255, 255, 255)
    
    DEALER_RECT = pygame.Rect(450, 80, 100, 100)
    NUM_CARDS_DEALER  = 10
    
    DECK_RECT = pygame.Rect(570, 130, CARD_RECT_WIDTH, CARD_RECT_HEIGHT)    
    
    FONT_CARD_PATH = 'fonts/arial-unicode-ms.ttf'
    FONT_TITLE_PATH = 'fonts/blackjackregular.ttf'
    FONT_PATH = 'fonts/arial-unicode-ms.ttf'
    FONT_NAME_PATH = 'fonts/montserrat.otf'
    
    DEALING_CARD_SOUND_PATH = 'files/sounds/dealing-card.wav'
    SHUFFLING_CARD_SOUND_PATH = 'files/sounds/huffling-cards-01.wav'
    
    def __init__(self, players):
        
        self.players = players
        self.hand_dealer_rects = []
        self.hand_player_rects = []
        
        # inicializa as variáveis de estado do jogo
        self.game_state = None
        self.previous_game_state = None
                
        # Inicializa o Pygame
        self.init_pygame()
        
        # Carrega o som de uma carta
        self.load_resources()
                       
        # Cria uma nova janela
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # Define o título da janela
        pygame.display.set_caption('Blackjack em Python')

        # Define a cor da mesa de blackjack e o fundo da tela
        self.BLACKJACK_TABLE_COLOR = (0, 128, 0)  # verde escuro
        self.TABLE_BORDER_COLOR = (0, 0, 0)  # preto
        self.BACKGROUND_COLOR = (0, 100, 0)  # verde mais claro
        self.screen.fill(self.BACKGROUND_COLOR)
        
        # Define a fonte e o tamanho do texto do título
        self.title_font = pygame.font.Font(self.FONT_TITLE_PATH, 80)
        self.title_text = self.title_font.render("BlackJack em Python", True, (255, 255, 255))
        
        self.update_screen()
    
    def init_pygame(self):
        pygame.init()
        pygame.mixer.init()
        
    def load_resources(self):       
        try:
            self.card_sound = pygame.mixer.Sound(self.DEALING_CARD_SOUND_PATH)
            self.shuffling_card_sound = pygame.mixer.Sound(self.SHUFFLING_CARD_SOUND_PATH)
            # outros arquivos de som
        except pygame.error as e:
            print(f"Erro ao carregar arquivo de som: {e}")

    def draw_title(self):
        # Obtém a posição central do texto do título
        title_rect = self.title_text.get_rect(center=(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))

        # Desenha o texto do título em negrito no meio da tela
        pygame.draw.rect(self.screen, self.BACKGROUND_COLOR, title_rect)
        self.screen.blit(self.title_text, title_rect)

    def draw_dealer(self):
        self.draw_dealer_space()
        self.draw_dealer_hand()
        self.draw_deck()

    def draw_dealer_space(self):
        # Desenha o espaço para o dealer
        pygame.draw.rect(self.screen, self.TABLE_BORDER_COLOR, self.DEALER_RECT, 2)
        pygame.draw.rect(self.screen, self.COLOR_FONT_DEFAULT, self.DEALER_RECT, 2)

    def draw_dealer_hand(self):
        # Desenha os espaços para as cartas da mão do dealer
        self.hand_dealer_rects = []
        x_offset = 280
        y_offset = self.DEALER_RECT.top + self.DEALER_RECT.height + 20

        for i in range(self.NUM_CARDS_DEALER):
            hand_rect = pygame.Rect(x_offset + i * (self.CARD_RECT_WIDTH + 5), y_offset, self.CARD_RECT_WIDTH, self.CARD_RECT_HEIGHT)
            self.hand_dealer_rects.append(hand_rect)
            pygame.draw.rect(self.screen, self.TABLE_BORDER_COLOR, hand_rect, 2)
            
    def draw_deck(self):
        # Desenha o retângulo para o baralho
        pygame.draw.rect(self.screen, self.TABLE_BORDER_COLOR, self.DECK_RECT, 2)
        pygame.draw.rect(self.screen, self.COLOR_FONT_DEFAULT, self.DECK_RECT, 2)

    def draw_players(self):
        player_rects = []
        self.hand_player_rects = []
        
        total_player_width = (self.PLAYER_HAND_WIDTH + self.PLAYER_HAND_SPACING) * 8 - self.PLAYER_HAND_SPACING
        x_offset = (self.WINDOW_WIDTH - total_player_width) // 2
        y_offset = self.WINDOW_HEIGHT - self.PLAYER_HAND_HEIGHT - 50
        
        for i in range(8):
            if i >= len(self.players):
                continue

            player_rect = pygame.Rect(x_offset + i * (self.PLAYER_HAND_WIDTH + self.PLAYER_HAND_SPACING), y_offset, self.PLAYER_HAND_WIDTH, self.PLAYER_HAND_HEIGHT)
            player_rects.append(player_rect)

            self.draw_player_rect(player_rect)
            self.draw_text_on_screen(self.players[i].get_user().name, self.FONT_NAME_PATH, 15, self.COLOR_FONT_DEFAULT, player_rect.centerx, player_rect.bottom + 5, self.screen)
            self.draw_text_on_screen('${:,.2f}'.format(self.players[i].get_user().balance), self.FONT_NAME_PATH, 15, self.COLOR_FONT_DEFAULT, player_rect.centerx, player_rect.bottom + 25, self.screen)
            self.draw_player_cards(player_rect)

    def draw_player_rect(self, player_rect):
        # Desenha o retângulo do jogador
        pygame.draw.rect(self.screen, self.BLACKJACK_TABLE_COLOR, player_rect)
        pygame.draw.rect(self.screen, self.TABLE_BORDER_COLOR, player_rect, 2)
        
    def draw_text_on_screen(self, text, font_path:str, size:int, color, x:int, y:int, surface):
        font = pygame.font.Font(font_path, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(centerx=x, top=y)
        surface.blit(text_surface, text_rect)

    def draw_player_cards(self, player_rect):
        # Desenha os espaços para as cartas do jogador
        card_rect_width = self.CARD_RECT_WIDTH
        card_rect_height = self.CARD_RECT_HEIGHT
        card_rect_spacing = 10
        card_rect1 = pygame.Rect(player_rect.left + 10, player_rect.top - card_rect_height - card_rect_spacing, card_rect_width, card_rect_height)
        card_rect2 = pygame.Rect(player_rect.left + 10 + card_rect_width + card_rect_spacing, player_rect.top - card_rect_height - card_rect_spacing,
                                    card_rect_width, card_rect_height)

        pygame.draw.rect(self.screen, (255, 255, 255), card_rect1, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), card_rect2, 2)

        self.hand_player_rects.append( HandPlayerRect(self.players[0], [card_rect1, card_rect2]))
                             
    def draw_card(self, x, y, value, suit):
        # Define o tamanho da carta
        card_width = self.CARD_RECT_WIDTH - 10
        card_height = self.CARD_RECT_HEIGHT - 10

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
        
    def draw_table(self):
        self.draw_dealer()
        self.draw_players()

        for rect in self.hand_dealer_rects:
            self.draw_card(rect.x+5, rect.y+5, 7, '♣')

            for rect in self.hand_player_rects:
                rect0 = rect.get_rects()[0]
                rect1 = rect.get_rects()[1]
                #pygame.time.set_timer(pygame.USEREVENT, 3000)
                #self.card_sound.play()
                
                self.draw_card(rect0.x+5, rect0.y+5, 7, '♥')
                self.draw_card(rect0.x+10, rect0.y-5, 10, '♣')
                self.draw_card(rect0.x+15, rect0.y-15, 10, '♥')
                self.draw_card(rect0.x+20, rect0.y-25, 10, '♣')

                self.draw_card(rect1.x+5, rect1.y+5, 'K', '♣')
                self.draw_card(rect1.x+10, rect1.y-5, 10, '♣')
                self.draw_card(rect1.x+15, rect1.y-15, 10, '♥')
                self.draw_card(rect1.x+20, rect1.y-25, 10, '♣')

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

            # verifica se houve mudanças no estado do jogo
            print(f" {self.game_state} - {self.previous_game_state}")
            if self.game_state != self.previous_game_state:
                # chama os métodos de desenho apenas se houve mudanças
                self.update_screen()
                # atualiza o estado anterior do jogo
                self.previous_game_state = self.game_state
    
    def update_screen(self):
        # chama os métodos de desenho necessários
        self.draw_title()
        self.draw_table()
    
    # os outros métodos da classe

    def start_game(self):
        # inicia o jogo e atualiza o estado do jogo
        self.shuffling_card_sound.play()
        self.game_state = "playing"

    def deal_cards(self):
        # distribui as cartas e atualiza o estado do jogo
        self.game_state = "dealing"

    def hit_player(self):
        # compra uma carta para o jogador e atualiza o estado do jogo
        self.game_state = "hitting"

    def stand_player(self):
        # jogador para de comprar cartas e atualiza o estado do jogo
        self.game_state = "standing"

    def end_round(self):
        # finaliza a rodada e atualiza o estado do jogo
        for player in self.players:
            player.get_user().update_balance(Result.LOSS, 199)
        self.game_state = "ending_round"