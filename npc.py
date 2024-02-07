import pygame

import config


class Npc:
    def __init__(self, name, image,  x_position, y_position):
        print("Npc created")
        self.name = name
        self.position = [x_position, y_position]
        self.image = pygame.image.load("images/" + str(image) + ".png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        self.animative = None
        self.animatives = []
    def update(self):
        print("Npc updated")

    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]

    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)
