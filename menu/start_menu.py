import json
import sys
from data.config import screen
from game_setting import setting
from game_things import info
from sprites.config import *
from sprites.environment.coin import Coin
from sprites.funk.game import create_space
from sprites.menu.ball_on_ship import BallOnShip
from sprites.menu.logotip import Logotip
from sprites.menu.btn_exit import BtnExit
from sprites.menu.btn_start import BtnStart
from sprites.menu.fon import Fon
from sprites.menu.shop.shop import Shop
from sprites.menu.shop.btn_ship import BtnShip
from sprites.menu.shop.btn_specifications import BtnSpecific
from sprites.menu.shop.ships.bth_buy_ship import BtnBuyShip
from sprites.menu.view_choice_ship import ViewSpaceShip
from sprites.menu.shop.ships.choice_ship import ChoiceShip
from sprites.menu.shop.ships.close_ship import CloseShip
from sprites.menu.shop.specific.bth_buy_specific import BtnBuySpecific
from sprites.menu.shop.specific.specific import Specific
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
    magaz, btn_specific, btn_ship = view_magaz()
    view_ships(magaz)
    Fon()
    Logotip()
    icon_shop = Shop(magaz.rect.center)
    okno_choice_ship = ViewSpaceShip(d_w=0.54, d_h=0.4)
    okno_center_x = okno_choice_ship.rect.x + okno_choice_ship.rect.w // 2
    okno_center_y = okno_choice_ship.rect.y + okno_choice_ship.rect.h // 2
    BallOnShip(okno_center_x, okno_center_y)
    coins = Coin(okno_center_x * 0.88, okno_choice_ship.rect.y * 0.85)
    btn_start = BtnStart(okno_center_x, okno_center_y)
    btn_exit = BtnExit(okno_center_x, okno_center_y, menu_sprites)
    ship = MenuSpaceShip(info['ship_type'], okno_center_x, okno_center_y)
    while running:
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_start.rect.collidepoint(event.pos):
                    menu_sprites.empty()
                    coins.remove(all_sprites)
                    for meteor in meteors_sprites:
                        meteor.kill()
                    return
                if btn_specific.rect.collidepoint(event.pos) and \
                        not menu_specific_sprites.sprites():
                    for sprite in choice_ship_sprites:
                        sprite.kill()
                    view_specific(magaz)
                    icon_shop.kill()
                    icon_shop = Shop(magaz.rect.center)
                if btn_ship.rect.collidepoint(event.pos) and not choice_ship_sprites.sprites():
                    for sprite in menu_specific_sprites:
                        sprite.kill()
                    view_ships(magaz)
                    icon_shop.kill()
                    icon_shop = Shop(magaz.rect.center)
                if btn_exit.rect.collidepoint(event.pos):
                    terminate()
                for ikon in menu_ships_sprites:
                    if ikon.rect.collidepoint(event.pos) and ikon.enable:
                        ship.kill()
                        info['ship_type'] = ikon.ship_type
                        ship = MenuSpaceShip(info['ship_type'], okno_center_x, okno_center_y)
            events.append(event)
        menu_sprites.update(*events)
        menu_sprites.draw(screen)
        view_all_koins(info['koins'], okno_choice_ship)
        pygame.display.flip()
        clock.tick(FPS)


def view_magaz():
    window = ChoiceShip()
    btn_spesific = BtnSpecific(window.rect)
    btn_ship = BtnShip(window.rect)
    return window, btn_spesific, btn_ship


def view_ships(window):
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
                BtnBuyShip(x, y + window.rect.h * 0.19, setting[f'ship_{ship_type}_price'],
                           ship_type)
                CloseShip(x, y, ship_type)
                ship.enable = False


def view_specific(window):
    x_s = window.rect.x + window.rect.w // 4
    x_e = window.rect.x + window.rect.w
    y_s = window.rect.y + window.rect.h // 4
    y_e = window.rect.y + window.rect.h
    delta = window.rect.h * 0.04
    specifics = ['weapon_damage', 'hp_max', 'power_magnet']
    type_specific = 0
    for y_n, y in enumerate(range(y_s, int(y_e - delta), int(window.rect.h // 2 - delta))):
        for x_n, x in enumerate(range(x_s, int(x_e - delta), window.rect.w // 2)):
            type_specific += 1
            if type_specific > len(specifics):
                return
            specific = Specific(x, y, specifics[type_specific - 1])
            price = setting[f'specific_{specifics[type_specific - 1]}_price']
            power = setting[f'specific_{specifics[type_specific - 1]}_power']
            BtnBuySpecific(x, y + window.rect.h * 0.19, price, power, specific)


def view_all_koins(koins, okno):
    font = pygame.font.Font(None, 50)
    string_rendered = font.render(f'{koins}', 1, (255, 255, 255))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = okno.rect.x + okno.rect.w // 2 - intro_rect.w // 2
    intro_rect.y = okno.rect.y * 0.76
    screen.blit(string_rendered, intro_rect)
