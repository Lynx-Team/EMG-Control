import pygame
from space_game import game as space_game
from setup_menu import start_setup
import space_game.game_config as config
import flappy_bird.game as flappy 

def main(mode):
    pygame.init()
    size = (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(config.WINDOW_CAPTION)

    start_setup(screen)

    if mode == 'space_game':
        space_game.start_game(screen)
    elif mode == 'flappy':
        pygame.display.quit()
        pygame.quit()
        flappy.start_game('flappy_bird\\flappy_bird.exe')

if __name__ == '__main__':
    main('flappy')