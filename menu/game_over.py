import pygame

from data.config import screen, FPS, width, height
import game_things
from game_things import info
from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites, shot_sprites, \
    game_over_sprites, game_pause_sprites
from sprites.funk.game import view_koins
from sprites.menu.game_over import GameOver
from menu.start_menu import terminate, start_screen


def clear_sprites_group():
    all_sprites.empty()
    menu_sprites.empty()
    player_sprites.empty()
    meteors_sprites.empty()
    shot_sprites.empty()
    game_pause_sprites.empty()


def game_over():
    pygame.mouse.set_visible(True)
    clear_sprites_group()
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    GameOver()
    koins = game_things.game_koins
    game_things.game_koins = 0
    info['koins'] += koins
    view_koins(koins)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                start_screen()
                return
        game_over_sprites.update()
        game_over_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
