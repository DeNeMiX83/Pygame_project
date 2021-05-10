from time import sleep

import pygame

from game import game_things
from data.config import height, FPS, screen, width
from sprites.environment.meteor import Meteor
from sprites.environment.space import Space
from sprites.player.lvl_1.lvl1 import ShipLevel1
from sprites.player.lvl_2.lvl_2 import ShipLevel2
from sprites.player.lvl_3.lvl_3 import ShipLevel3
from sprites.player.lvl_4.lvl_4 import ShipLevel4


def create_space():
    Space(0 - height)
    Space(0)


def get_space_ship(type):
    ship = None
    damage = game_things.info[f'ship_{type}']['damage']
    weapon_damage = game_things.info[f'ship_{type}']['weapon_damage']
    power_magnet = game_things.info[f'ship_{type}']['power_magnet']
    hp_max = game_things.info[f'ship_{type}']['hp_max']
    if type == 1:
        ship = ShipLevel1(type, damage, weapon_damage, power_magnet, hp_max)
    if type == 2:
        ship = ShipLevel2(type, damage, weapon_damage, power_magnet, hp_max)
    if type == 3:
        ship = ShipLevel3(type, damage, weapon_damage, power_magnet, hp_max)
    if type == 4:
        ship = ShipLevel4(type, damage, weapon_damage, power_magnet, hp_max)
    return ship


def view_koins(d_x=0.49, d_y=0.6, font_size=50, x_center=True, y_center=False):
    koins = game_things.game_koins
    font = pygame.font.Font(None, font_size)
    string_rendered = font.render(f'Собрано монет: {koins}', 1, (255, 255, 255))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = width * d_x - (intro_rect.w // 2 if x_center else 0)
    intro_rect.y = height * d_y - (intro_rect.h // 2 if y_center else 0)
    screen.blit(string_rendered, intro_rect)


def view_score(d_x=0.49, d_y=0.6, font_size=50, x_center=True, y_center=False):
    score = game_things.game_score
    font = pygame.font.Font(None, font_size)
    string_rendered = font.render(f'Счет: {score}', 1, (255, 255, 255))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = width * d_x - (intro_rect.w // 2 if x_center else 0)
    intro_rect.y = height * d_y - (intro_rect.h // 2 if y_center else 0)
    screen.blit(string_rendered, intro_rect)

