from space_object import SpaceObject
import game_config as config

class Bullet(SpaceObject):
    def __init__(self, x, y):
        super().__init__('assets/bullet.png', x, y)

    def update(self):
        self.rect.y -= config.BULLET_SPEED
