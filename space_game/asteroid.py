import pygame
from space_object import SpaceObject
import game_config as config
import random

class Asteroid(SpaceObject):
    def __init__(self):
        rand_img_id = random.randint(1, 4)
        super().__init__('assets/asteroid_' + str(rand_img_id) + '.png', config.ASTEROID_WIDTH, config.ASTEROID_HEIGHT, 0, 0)

        rand_angle = random.randint(1, 360)
        self.image = pygame.transform.rotate(self.image, rand_angle)

        self.speed = config.ASTEROID_MIN_SPEED + (config.ASTEROID_MAX_SPEED - config.ASTEROID_MIN_SPEED) * random.random()
        self.rect.x = random.randint(0, config.WINDOW_WIDTH - config.ASTEROID_WIDTH)

    def update(self):
        self.rect.y += self.speed
