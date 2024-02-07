import pygame
import configanimative

class Animative:
    def __init__(self, animative_type, id):
        self.type = animative_type
        self.health = 10
        self.attack = 10
        self.id = id
        self.image = pygame.image.load("images/animatives/" + f"{self.id:03d}" + ".png")
        self.flipped = pygame.image.load("images/animatives/" + f"{self.id:03d}" + "flipped.png")
        self.battle = pygame.image.load("images/animatives/" + f"{self.id:03d}" + "battle.png")

        self.name = configanimative.ANIMATIVES[id]['name']

