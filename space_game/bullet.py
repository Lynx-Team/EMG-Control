from space_game.space_object import SpaceObject
import space_game.game_config as config

class Bullet(SpaceObject):
    def __init__(self, x, y):
        super().__init__('space_game/assets/bullet.png', x, y)

    def update(self):
        self.rect.y -= config.BULLET_SPEED
