from space_object import SpaceObject
from bullet import Bullet
import game_config as config

class SpaceShip(SpaceObject):
    def __init__(self):
        super().__init__('assets/spaceship.png', config.WINDOW_WIDTH / 2  - config.SHIP_WIDTH / 2, config.WINDOW_HEIGHT - config.SHIP_HEIGHT)

    def move_left(self):
        if not (self.rect.x - config.SHIP_MOVE_DX < 0):
            self.rect.x -= config.SHIP_MOVE_DX

    def move_right(self):
        if not (self.rect.x + config.SHIP_WIDTH + config.SHIP_MOVE_DX > config.WINDOW_WIDTH):
            self.rect.x += config.SHIP_MOVE_DX
    
    def move(self, movement):
        if len(movement) < 2:
            return

        movement = movement[1]

        if movement == '1':
            self.move_left()
            return None
        elif movement == '2':
            self.move_right()
            return None
        elif movement == '3':
            return Bullet(self.rect.x + config.SHIP_WIDTH // 2 - config.BULLET_WIDTH // 2, config.WINDOW_HEIGHT - config.SHIP_HEIGHT)
