import pygame
import data_handler.arduino as arduino
import space_game.game_config as config

def start_setup(screen):
    font = pygame.font.SysFont(config.FONT_FAMILY, config.FONT_SIZE)
    isSetup = False

    while not isSetup:
        count_for_setup = arduino.get_data()

        if (len(count_for_setup) < 2):
            continue

        if count_for_setup[0] != 'S':
            isSetup = True
            break

        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                isSetup = True
                break

        text_setup = font.render(config.SETUP_TEXT.format(count_for_setup[1]), True, config.WHITE)

        screen.fill(config.BLACK)
        screen.blit(text_setup, (config.WINDOW_WIDTH / 2 - text_setup.get_width() / 2, config.WINDOW_HEIGHT / 2 - text_setup.get_height() / 2))
        pygame.display.flip()
