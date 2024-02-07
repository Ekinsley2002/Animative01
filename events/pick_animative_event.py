import pygame
import config
from game_state import GameState
from animative_factory import AnimativeFactory

class PickAnimativeEvent:
    def __init__(self, screen, game, player, animative):
        self.screen = screen
        self.game = game
        self.player = player
        self.animative_factory = AnimativeFactory()
        self.diolog2 = pygame.image.load("images/diolog2.png")
        self.diolog3 = pygame.image.load("images/diolog3.png")

        if animative.name == "animativeF_capsul":
            self.animative = self.animative_factory.create_animative_index(1)

        elif animative.name == "animativeG_capsul":
            self.animative = self.animative_factory.create_animative_index(4)

        elif animative.name == "animativeW_capsul":
            self.animative = self.animative_factory.create_animative_index(7)


        self.cut = 0
        self.max_cut = 0

    def load(self):
        pass
    def render(self):
        if self.cut == 0:
            self.render_scene0()

    def render_scene0(self):
        self.screen.blit(self.diolog2, (0, 150))
        self.screen.blit(self.diolog3, (520, 175))
        self.screen.blit(self.animative.image, (600, -20))
        font = pygame.font.Font("pokemon_pixel_font.ttf", 40)
        img = font.render("You picked..." + str(self.animative.name), True, config.BLACK)
        self.screen.blit(img, (250, 400))
        img2 = font.render("Are you sure you want this animative?", True, config.BLACK)
        self.screen.blit(img2, (250, 435))
        img3 = font.render("(y/n)", True, config.BLACK)
        self.screen.blit(img3, (770, 432))

        pass
    def update(self):

        if self.cut > self.max_cut:
            self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
                #handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                elif event.key == pygame.K_y:
                    self.player.animatives.append(self.animative)
                    self.game.event = None
                elif event.key == pygame.K_n:
                    self.game.event = None


