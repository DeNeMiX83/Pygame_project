import time

import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, menu_sprites, choice_ship_sprites, menu_ships_sprites


class ViewSpaceShip(pygame.sprite.Sprite):
    def __init__(self, d_w=0.21, d_h=0.49):
        super(ViewSpaceShip, self).__init__(menu_sprites)
        self.image = load_image(['menu', 'choice_ship.png'])
        self.rect = self.image.get_rect()
        self.rect.x = width * d_w - self.rect.w // 2
        self.rect.y = height * d_h - self.rect.h // 2