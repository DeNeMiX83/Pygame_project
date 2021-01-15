import pygame

from data.config import screen, FPS, width, height
import game_things
from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites, shot_sprites
from sprites.menu.game_over import GameOver
from start_menu import terminate, start_screen


def view_koins(koins):
    font = pygame.font.Font(None, 50)
    string_rendered = font.render(f'Собрано монет: {koins}', 1, (255, 255, 255))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = width * 0.49 - intro_rect.w // 2
    intro_rect.y = height * 0.6
    screen.blit(string_rendered, intro_rect)


def clear_sprites_group():
    all_sprites.empty()
    menu_sprites.empty()
    player_sprites.empty()
    meteors_sprites.empty()
    shot_sprites.empty()


def game_over(ship_type):
    pygame.mouse.set_visible(True)
    clear_sprites_group()
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    GameOver()
    koins = game_things.koins
    game_things.info['koins'] += koins
    view_koins(koins)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return start_screen(screen, ship_type)
        menu_sprites.update()
        menu_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
