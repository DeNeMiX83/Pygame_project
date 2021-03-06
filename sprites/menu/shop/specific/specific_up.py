import time

import pygame

from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, player_sprites, menu_sprites


class SpecificUp(BaseAnimateSprite):
    def __init__(self, x, y):
        super(SpecificUp, self).__init__(menu_sprites)
        columns, rows = 15, 1
        self.image = load_image(['menu', f'specific_up.png'])
        self.resize(0.3)
        self.cut_sheet(self.image, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h * 0.68
        self.time_tik = 0.03
        self.put_timer()

    def update(self, *arg):
        if time.time() <= self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.put_timer()
        if self.cur_frame == len(self.frames) - 1:
            self.kill()