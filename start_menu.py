import sys
from random import choice

import game_things
from data.config import width, height, screen
import pygame

from game_things import info
from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites, shot_sprites, \
    choice_ship_sprites
from sprites.environment.koin import Koin
from sprites.funk.game import create_space
from sprites.menu.btn_exit import BtnExit
from sprites.menu.btn_start import BtnStart
from sprites.menu.choice_ship import ChoiceShip
from sprites.menu.game_over import GameOver
from sprites.menu.view_space_ship import ViewSpaceShip
from sprites.player.menu_ship import MenuSpaceShip
from sprites.player.show_ship import ShowShip

FPS = 100
running = True
ship = None


def terminate():
    with open('data\save', 'w') as f:
        for name, value in info.items():
            f.write(f'{name}={value}')
    pygame.quit()
    sys.exit()


def start_screen(screen, ship_type=1):
    space_ship_type = ship_type
    clock = pygame.time.Clock()
    create_space()
    koins = Koin(width * 0.43, height * 0.14)
    view_ships()
    ViewSpaceShip(space_ship_type)
    btn_start = BtnStart()
    btn_exit = BtnExit()
    ship = MenuSpaceShip(space_ship_type)
    while running:
        event = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_start.rect.collidepoint(event.pos):
                    menu_sprites.empty()
                    koins.remove(all_sprites)
                    return space_ship_type
                if btn_exit.rect.collidepoint(event.pos):
                    terminate()
                for ikon in choice_ship_sprites:
                    if ikon.rect.collidepoint(event.pos):
                        ship.kill()
                        space_ship_type = ikon.type_ship
                        ship = MenuSpaceShip(space_ship_type)
            menu_sprites.update(event)
        if not event:
            menu_sprites.update()
        menu_sprites.draw(screen)
        view_all_koins(game_things.info['koins'])
        pygame.display.flip()
        clock.tick(FPS)


def view_ships():
    window = ChoiceShip()
    x_s = window.rect.x + window.rect.w // 4
    x_e = window.rect.x + window.rect.w
    y_s = window.rect.y + window.rect.h // 4
    y_e = window.rect.y + window.rect.h
    ship_type = 0
    for y_n, y in enumerate(range(y_s, y_e, window.rect.h // 2)):
        for x_n, x in enumerate(range(x_s, x_e, window.rect.w // 2)):
            ship_type += 1
            ViewSpaceShip(ship_type, x, y)
            ShowShip(x, y, ship_type)


def view_all_koins(koins):
    font = pygame.font.Font(None, 50)
    string_rendered = font.render(f'{koins}', 1, (255, 255, 255))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = width * 0.46 - intro_rect.w // 2
    intro_rect.y = height * 0.116
    screen.blit(string_rendered, intro_rect)