import time
from random import choice

import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import menu_sprites, menu_ships_sprites


class Shop(BaseAnimateSprite):
    def __init__(self, center):
        super(Shop, self).__init__(menu_sprites)
        columns, rows = 2, 1
        sheet = load_image(['menu', f'magaz.png'])
        self.cut_sheet(sheet, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.rect.center = center
        self.rect.x -= self.rect.w * 0.01
        self.rect.y += self.rect.h * 0.01
        self.time_tik = 1
        self.put_timer()

    def update(self, *arg):
        if time.time() < self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.time_tik = choice(list(map(lambda x: x / 10, range(1, 20))))
        self.put_timer()