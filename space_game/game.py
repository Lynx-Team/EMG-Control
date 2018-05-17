import pygame
import game_config as config
from space_ship import SpaceShip
from asteroid import Asteroid
import data_handler.arduino as arduino

pygame.init()

font = pygame.font.SysFont(config.FONT_FAMILY, config.FONT_SIZE)
background = pygame.image.load('assets/bg.jpg')

size = (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption(config.WINDOW_CAPTION)

all_sprites_list = pygame.sprite.Group()
all_asteroids = pygame.sprite.Group()

space_ship = SpaceShip()
all_sprites_list.add(space_ship)

carryOn = True
isSetup = False
current_asteroid_time = 0
score = 0
clock = pygame.time.Clock()

# First setup

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
            carryOn = False
            break

        if (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            isSetup = True
            break

    text_setup = font.render(config.SETUP_TEXT + ', ' + count_for_setup[1] + ' times left.', True, config.WHITE)

    screen.fill(config.BLACK)
    screen.blit(text_setup, (config.WINDOW_WIDTH / 2 - text_setup.get_width() / 2, config.WINDOW_HEIGHT / 2 - text_setup.get_height() / 2))
    pygame.display.flip()
    clock.tick(30)

while carryOn:

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False

    space_ship.move(arduino.get_data())

    # Logic

    for astr in all_asteroids:
        if astr.rect.y >= config.WINDOW_HEIGHT:
            score += 1
            all_asteroids.remove(astr)

    current_asteroid_time += 1
    if current_asteroid_time >= config.ASTEROID_INTERVAL:
        new_asteroid = Asteroid()
        all_sprites_list.add(new_asteroid)
        all_asteroids.add(new_asteroid)
        current_asteroid_time = 0

    collision_list = pygame.sprite.spritecollide(space_ship, all_asteroids, False)
    for i in collision_list:
        print(config.GAME_OVER_TEXT)
        carryOn = False

    all_sprites_list.update()

    # Draw

    text_score = font.render(config.SCORE_TEXT + str(score), True, config.BLUE)

    screen.fill(config.BLACK)
    screen.blit(background, (0, 0))
    screen.blit(text_score, (5, 5))
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
