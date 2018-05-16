import pygame
import game_config as config
from space_ship import SpaceShip
from asteroid import Asteroid

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
current_asteroid_time = 0
score = 0
clock = pygame.time.Clock()

while carryOn:
    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        space_ship.move_left()
    if keys[pygame.K_RIGHT]:
        space_ship.move_right()

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
