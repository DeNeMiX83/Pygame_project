import time

import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.base_time import BaseTime
from sprites.config import menu_sprites, menu_ships_sprites
from sprites.environment.meteor import Meteor


class Fon(BaseTime):
    def __init__(self):
        super(Fon, self).__init__(menu_sprites)
        self.image = pygame.transform.scale(load_image(['menu', 'fon.png']), (width, height))
        self.rect = self.image.get_rect()
