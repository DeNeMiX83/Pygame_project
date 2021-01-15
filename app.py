import asyncio
import threading
from time import sleep

from data.config import *
from game_things import koins
from sprites.config import all_sprites, player_sprites
from sprites.funk.game import create_meteor, get_space_ship
from start_menu import start_screen, game_over


def check_event():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player_sprites.update(event)
    all_sprites.update()


if __name__ == '__main__':
    size = width, height = size
    screen = screen
    koins = 0
    ship_type = start_screen(screen)
    player = get_space_ship(ship_type)
    pygame.mouse.set_visible(False)
    running = True
    clock = pygame.time.Clock()
    create_meteor()
    while running:
        screen.fill((0, 0, 0))
        if not player.alive():
            player = get_space_ship(game_over(ship_type))
        check_event()
        all_sprites.draw(screen)
        create_meteor()
        pygame.display.flip()
        clock.tick(FPS)
    # meteor_thread.join()
    pygame.quit()
