import pygame
from space_game.space_object import SpaceObject
import space_game.game_config as config
import random

class Asteroid(SpaceObject):
    def __init__(self):
        rand_img_id = random.randint(1, 4)
        super().__init__('space_game/assets/asteroid_' + str(rand_img_id) + '.png', 0, 0)

        self.angle = random.randint(1, 360)
        self.image = pygame.transform.rotate(self.image, self.angle)

        self.speed = config.ASTEROID_MIN_SPEED + (config.ASTEROID_MAX_SPEED - config.ASTEROID_MIN_SPEED) * random.random()
        self.rect.x = random.randint(0, config.WINDOW_WIDTH - config.ASTEROID_WIDTH)

    def update(self):
        self.rect.y += self.speed
