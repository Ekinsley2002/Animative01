import pygame
import config
from game_state import GameState

class ProfPickAnimativeEvent:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.prof_image = pygame.image.load("images/prof.png")
        self.prof_diolog = pygame.image.load("images/diolog.png")
        self.prof_diolog2 = pygame.image.load("images/diolog2.png")

        self.cut = 0
        self.max_cut = 2

    def load(self):
        pass
    def render(self):
        if self.cut == 0:
            self.render_scene0()

        if self.cut == 1:
            self.render_scene1()

        if self.cut == 2:
            self.render_scene2()

    def render_scene0(self):
        self.screen.blit(self.prof_image, (350, 0))
        self.screen.blit(self.prof_diolog, (0, 150))
        font = pygame.font.Font("pokemon_pixel_font.ttf", 40)
        img = font.render("Hello! It is good to see you!", True, config.BLACK)
        self.screen.blit(img, (275, 425))

        pass

    def render_scene1(self):
        self.screen.blit(self.prof_image, (350, 0))
        self.screen.blit(self.prof_diolog2, (0, 150))
        font = pygame.font.Font("pokemon_pixel_font.ttf", 40)
        img = font.render("Although I can't see much these days...", True, config.BLACK)
        self.screen.blit(img, (230, 425))

    def render_scene2(self):
        self.screen.blit(self.prof_image, (350, 0))
        self.screen.blit(self.prof_diolog2, (0, 150))
        font = pygame.font.Font("pokemon_pixel_font.ttf", 40)
        img = font.render("Anyways, pick your very own Animative!", True, config.BLACK)
        self.screen.blit(img, (230, 425))

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
                if event.key == pygame.K_RETURN:
                    self.cut = self.cut + 1


