import pygame
import config
import math
import utilities
from game_state import GameState

class Battle:
    def __init__(self, screen, animative, player):
        self.screen = screen
        self.animative = animative
        self.player = player


    def load(self):
        pass
    def render(self):
        self.forest_image = pygame.image.load("images/background_forest.png")
        rect_forest = pygame.Rect(-40, -32.5, 100, 100)
        self.screen.blit(self.forest_image, rect_forest)

        rect = pygame.Rect(800, 200, 2, 2)
        self.screen.blit(self.animative.battle, rect)

        self.screen.blit(self.player.battle, (320, 40))

        font = pygame.font.SysFont(None, 24)
        img = font.render("Health: " + str(self.animative.health) + "Attack: " + str(self.animative.attack), True, config.BLACK)
        self.screen.blit(img, (20, 220))

        img = font.render("Press enter to attack: " + str(self.animative.health), True, config.BLACK)
        self.screen.blit(img, (600, 1000))




    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            #handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.animative.health = self.animative.health - 1







