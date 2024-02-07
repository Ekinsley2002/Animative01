from player import Player
import pygame
from game import Game
import math
from game_state import GameState
import config
import utilities
class Menu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def set_up(self):
        self.menu_image = pygame.image.load("images/menu.png")
        self.logo_image = pygame.image.load("images/animative_logo.png")
        self.forest_image = pygame.image.load("images/forest.png")
        self.animative_image = pygame.image.load("images/animatives/002.png")
        self.animative_image2 = pygame.image.load("images/animatives/013.png")

    def update(self):
        self.screen.fill(config.BLACK)
        rect_start_button = pygame.Rect(300, 450, 1, 1)
        rect_logo = pygame.Rect(25, -275, 2, 2)
        rect_forest = pygame.Rect(-40, 1, 2, 2)
        rect_animative = pygame.Rect(700, 200, 2, 2)
        rect_animative2 = pygame.Rect(0, 200, 2, 2)
        self.screen.blit(self.forest_image, rect_forest)
        self.screen.blit(self.menu_image, rect_start_button)
        self.screen.blit(self.logo_image, rect_logo)
        self.screen.blit(self.animative_image, rect_animative)
        self.screen.blit(self.animative_image2, rect_animative2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
                #handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                elif event.key == pygame.K_SPACE: #Load game.update() if space is pressed
                    self.game.set_up()
                    self.game.game_state = GameState.RUNNING
