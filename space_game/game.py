import pygame
import space_game.game_config as config
from space_game.space_ship import SpaceShip
from space_game.asteroid import Asteroid
import data_handler.arduino as arduino

def start_game(screen):
    font = pygame.font.SysFont(config.FONT_FAMILY, config.FONT_SIZE)
    background = pygame.image.load('space_game/assets/bg.jpg')

    all_sprites_list = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()

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

        bullet = space_ship.move(arduino.get_data())
        if not bullet is None:
            all_sprites_list.add(bullet)
            all_bullets.add(bullet)

        # Logic

        for astr in all_asteroids:
            if astr.rect.y >= config.WINDOW_HEIGHT:
                score += 1
                astr.kill()

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

        for b in all_bullets:
            collision_list = pygame.sprite.spritecollide(b, all_asteroids, True)
            if collision_list:
                b.kill()

        all_sprites_list.update()

        # Draw

        text_score = font.render(config.SCORE_TEXT + str(score), True, config.BLUE)

        screen.fill(config.BLACK)
        screen.blit(background, (0, 0))
        screen.blit(text_score, (5, 5))
        all_sprites_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)
