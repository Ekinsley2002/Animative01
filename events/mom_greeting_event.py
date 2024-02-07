import pygame
import config
from game_state import GameState

class MomGreetingEvent:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.mom_image = pygame.image.load("images/mom2.png")
        self.mom_diolog = pygame.image.load("images/diolog.png")
        self.mom_diolog2 = pygame.image.load("images/diolog2.png")

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
        self.screen.blit(self.mom_image, (350, 0))
        self.screen.blit(self.mom_diolog, (0, 150))
        font = pygame.font.Font("pokemon_pixel_font.ttf", 40)
        img = font.render("Goodmorning! I hope you got a lot of sleep for your big day!", True, config.BLACK)
        self.screen.blit(img, (275, 425))

        pass

    def render_scene1(self):
        self.screen.blit(self.mom_image, (350, 0))
        self.screen.blit(self.mom_diolog2, (0, 150))
        font = pygame.font.Font("pokemon_pixel_font.ttf", 40)
        img = font.render("Today is the day you get your first Animative!", True, config.BLACK)
        self.screen.blit(img, (230, 425))

    def render_scene2(self):
        self.screen.blit(self.mom_image, (350, 0))
        self.screen.blit(self.mom_diolog2, (0, 150))
        font = pygame.font.Font("pokemon_pixel_font.ttf", 40)
        img = font.render("Make sure to talk to the professor at the lab!", True, config.BLACK)
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
