from space_object import SpaceObject
import game_config as config

class SpaceShip(SpaceObject):
    def __init__(self):
        super().__init__('assets/spaceship.png', config.SHIP_WIDTH, config.SHIP_HEIGHT,
            config.WINDOW_WIDTH / 2  - config.SHIP_WIDTH / 2, config.WINDOW_HEIGHT - config.SHIP_HEIGHT)

    def move_left(self):
        self.rect.x -= config.SHIP_MOVE_DX

    def move_right(self):
        self.rect.x += config.SHIP_MOVE_DX
