import time

import pygame

from data.config import width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites, menu_ships_sprites, choice_ship_sprites
from sprites.player.base_resize_sprite import BaseResize


class ShowShip(BaseResize):
    def __init__(self, x, y, type, enable=True):
        super(ShowShip, self).__init__(menu_sprites, menu_ships_sprites, choice_ship_sprites, dir='player')
        image = load_image(['player', f'lvl_{type}', f'lvl{type}.png'], -1)
        rect = image.get_rect()
        d_size = 1.5
        self.image_1 = pygame.transform.scale(image, (int(rect.w * d_size), int(rect.h * d_size)))
        d_size = 1.6
        self.image_2 = pygame.transform.scale(image, (int(rect.w * d_size), int(rect.h * d_size)))
        self.put_image()
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.enable = enable
        self.ship_type = type