import asyncio
import threading
from time import sleep

from data.config import *
from sprites.config import all_sprites, player_sprites
from sprites.funk.game import create_meteor
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
    player = start_screen(screen)
    pygame.mouse.set_visible(False)
    running = True
    clock = pygame.time.Clock()
    create_meteor()
    while running:
        screen.fill((0, 0, 0))
        if not player.alive():
            player = game_over()
        check_event()
        all_sprites.draw(screen)
        create_meteor()
        pygame.display.flip()
        clock.tick(FPS)
    # meteor_thread.join()
    pygame.quit()
