import time

import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, menu_sprites, choice_ship_sprites, menu_ships_sprites


class ViewSpaceShip(BaseAnimateSprite):
    def __init__(self, d_w=0.21, d_h=0.49):
        super(ViewSpaceShip, self).__init__(menu_sprites)
        columns, rows = 5, 1
        sheet = load_image(['menu', 'view_space_ship_3.png'])
        self.cut_sheet(sheet, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.rect.x = width * d_w - self.rect.w // 2
        self.rect.y = height * d_h - self.rect.h // 2
        self.time_tik = 0.1
        self.put_timer()

    def update(self, *args):
        if time.time() < self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.put_timer()
