from space_object import SpaceObject
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
        if movement[-1] == '1':
            if movement[0] == 'L':
                self.move_left()
            elif movement[0] == 'R':
                self.move_right()
