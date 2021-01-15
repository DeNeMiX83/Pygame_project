import time

import pygame

from data.config import width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites


class ShowShip(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super(ShowShip, self).__init__(menu_sprites)
        self.image = load_image(['player', f'lvl_{type}', f'lvl{type}.png'], -1)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2