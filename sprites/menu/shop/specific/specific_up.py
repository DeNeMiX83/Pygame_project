import time

import pygame

from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, player_sprites, menu_sprites


class SpecificUp(BaseAnimateSprite):
    def __init__(self, x, y):
        super(SpecificUp, self).__init__(menu_sprites)
        columns, rows = 15, 1
        sheet = load_image(['menu', f'specific_up.png'])
        rect = sheet.get_rect()
        d_size = 0.4
        sheet = pygame.transform.scale(sheet, (int(rect.w * d_size), int(rect.h * d_size)))
        self.cut_sheet(sheet, columns, rows)
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