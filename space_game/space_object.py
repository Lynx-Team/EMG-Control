import pygame
from pygame.sprite import Sprite
import game_config as config

class SpaceObject(Sprite):
    def __init__(self, image, width, height, start_x, start_y):
        super().__init__()

        self.image = pygame.Surface([width, height])

        pygame.draw.rect(self.image, image, [0, 0, width, height])
        self.rect = self.image.get_rect()

        self.rect.x = start_x
        self.rect.y = start_y
