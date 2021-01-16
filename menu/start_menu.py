import json
import sys
from random import choice

import game_things
from data.config import width, height, screen
import pygame

from game_setting import setting
from game_things import info
from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites, shot_sprites, \
    choice_ship_sprites, menu_ships_sprites
from sprites.environment.koin import Koin
from sprites.funk.game import create_space, create_meteor
from sprites.menu.bth_buy import BtnBuyShip
from sprites.menu.btn_exit import BtnExit
from sprites.menu.btn_start import BtnStart
from sprites.menu.choice_ship import ChoiceShip
from sprites.menu.close_ship import CloseShip
from sprites.menu.cosmonavt import Cosmonavt
from sprites.menu.game_over import GameOver
from sprites.menu.view_choice_ship import ViewSpaceShip
from sprites.player.menu_ship import MenuSpaceShip
from sprites.player.show_ship import ShowShip

FPS = 100
running = True
ship = None


def terminate():
    with open('data/save.json', 'w') as f:
        f.write(json.dumps(info, indent=4))
    pygame.quit()
    sys.exit()




def start_screen():
    clock = pygame.time.Clock()
    create_space()
    Cosmonavt()
    view_ships()
    okno_choice_ship = ViewSpaceShip(d_w=0.54, d_h=0.39)
    okno_center_x = okno_choice_ship.rect.x + okno_choice_ship.rect.w // 2
    okno_center_y = okno_choice_ship.rect.y + okno_choice_ship.rect.h // 2
    koins = Koin(okno_center_x * 0.88, okno_choice_ship.rect.y * 0.85)
    btn_start = BtnStart(okno_center_x, okno_center_y)
    btn_exit = BtnExit(okno_center_x, okno_center_y)
    ship = MenuSpaceShip(info['ship_type'], okno_center_x, okno_center_y)
    while running:
        events = []
        create_meteor()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_start.rect.collidepoint(event.pos):
                    menu_sprites.empty()
                    koins.remove(all_sprites)
                    return
                if btn_exit.rect.collidepoint(event.pos):
                    terminate()
                for ikon in menu_ships_sprites:
                    if ikon.rect.collidepoint(event.pos) and ikon.enable:
                        print(1)
                        ship.kill()
                        info['ship_type'] = ikon.ship_type
                        ship = MenuSpaceShip(info['ship_type'])
            events.append(event)
        menu_sprites.update(*events)
        menu_sprites.draw(screen)
        view_all_koins(info['koins'], okno_choice_ship)
        pygame.display.flip()
        clock.tick(FPS)


def view_ships():
    window = ChoiceShip()
    x_s = window.rect.x + window.rect.w // 4
    x_e = window.rect.x + window.rect.w
    y_s = window.rect.y + window.rect.h // 4
    y_e = window.rect.y + window.rect.h
    delta = window.rect.h * 0.04
    ship_type = 0
    for y_n, y in enumerate(range(y_s, int(y_e - delta), int(window.rect.h // 2 - delta))):
        for x_n, x in enumerate(range(x_s, int(x_e - delta), window.rect.w // 2)):
            ship_type += 1
            ship = ShowShip(x, y, ship_type)
            if info[f'ship_{ship_type}']['condition'] == 'close':
                BtnBuyShip(x, y + window.rect.h * 0.19, setting[f'ship_{ship_type}_price'], ship_type)
                CloseShip(x, y, ship_type)
                ship.enable = False


def view_all_koins(koins, okno):
    font = pygame.font.Font(None, 50)
    string_rendered = font.render(f'{koins}', 1, (255, 255, 255))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = okno.rect.x + okno.rect.w // 2 - intro_rect.w // 2
    intro_rect.y = okno.rect.y * 0.8
    screen.blit(string_rendered, intro_rect)