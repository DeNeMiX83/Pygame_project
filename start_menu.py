import sys
from random import choice
from data.config import width, height, screen
import pygame

from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites, shot_sprites, \
    choice_ship_sprites
from sprites.funk.game import create_space, get_space_ship
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
    pygame.quit()
    sys.exit()


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


def start_screen(screen, ship_type=1):
    space_ship_type = ship_type
    clock = pygame.time.Clock()
    create_space()
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


