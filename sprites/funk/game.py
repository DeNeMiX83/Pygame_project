from random import choice

from data.config import height, FPS, width
from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites, shot_sprites
from sprites.environment.meteor import Meteor
from sprites.environment.space import Space
from sprites.player.lvl_1.lvl1 import ShipLevel1
from sprites.player.space_ship import SpaceShip

cur_meteor = -1
max_meteor = 2
meteor_max_img = 2


def create_space():
    Space(0 - height)
    Space(0)


def show_space_ship(type):
    ship = None
    if type == 1:
        ship = ShipLevel1(type)
    return ship


def create_meteor():
    global cur_meteor
    cur_meteor += 1
    x = choice(range(0, width))
    y = choice(range(0 - height - 100, -100))
    if cur_meteor % (FPS / max_meteor) == 0:
        Meteor(x, y)

