from space_object import SpaceObject
import game_config as config
import random

class Asteroid(SpaceObject):
    def __init__(self):
        super().__init__(config.WHITE, config.ASTEROID_WIDTH, config.ASTEROID_HEIGHT, 0, 0)

        self.speed = config.ASTEROID_MIN_SPEED + (config.ASTEROID_MAX_SPEED - config.ASTEROID_MIN_SPEED) * random.random()
        self.rect.x = random.randint(0, config.WINDOW_WIDTH - config.ASTEROID_WIDTH)

    def update(self):
        self.rect.y += self.speed
