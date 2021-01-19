import pygame

from data.config import height, FPS, screen, width
from game_things import info
from sprites.environment.meteor import Meteor
from sprites.environment.space import Space
from sprites.player.lvl_1.lvl1 import ShipLevel1
from sprites.player.lvl_2.lvl_2 import ShipLevel2
from sprites.player.lvl_3.lvl_3 import ShipLevel3
from sprites.player.lvl_4.lvl_4 import ShipLevel4

cur_meteor = -1
max_meteor = 4
meteor_max_img = 2


def create_space():
    Space(0 - height)
    Space(0)


def get_space_ship(type):
    ship = None
    damage = info[f'ship_{type}']['damage']
    weapon_damage = info[f'ship_{type}']['weapon_damage']
    power_magnet = info[f'ship_{type}']['power_magnet']
    hp_max = info[f'ship_{type}']['hp_max']
    if type == 1:
        ship = ShipLevel1(type, damage, weapon_damage, power_magnet, hp_max)
    if type == 2:
        ship = ShipLevel2(type, damage, weapon_damage, power_magnet, hp_max)
    if type == 3:
        ship = ShipLevel3(type, damage, weapon_damage, power_magnet, hp_max)
    if type == 4:
        ship = ShipLevel4(type, damage, weapon_damage, power_magnet, hp_max)
    return ship


def create_meteor():
    global cur_meteor
    cur_meteor += 1
    if cur_meteor % (FPS / max_meteor) == 0:
        Meteor()


def view_koins(koins, d_x=0.49, d_y=0.6):
    font = pygame.font.Font(None, 50)
    string_rendered = font.render(f'Собрано монет: {koins}', 1, (255, 255, 255))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = width * d_x - intro_rect.w // 2
    intro_rect.y = height * d_y - intro_rect.h // 2
    screen.blit(string_rendered, intro_rect)

