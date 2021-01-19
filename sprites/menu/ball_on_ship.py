import time

import pygame

from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, player_sprites, menu_sprites


class BallOnShip(BaseAnimateSprite):
    def __init__(self, x, y):
        super(BallOnShip, self).__init__(menu_sprites)
        columns, rows = 10, 3
        sheet = load_image(['menu', f'ball.png'])
        rect = sheet.get_rect()
        d_size = 0.8
        sheet = pygame.transform.scale(sheet, (int(rect.w * d_size), int(rect.h * d_size)))
        self.cut_sheet(sheet, columns, rows)
        del self.frames[-1]
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y * 1.1 - self.rect.h // 2
        self.time_tik = 0.13
        self.put_timer()

    def update(self, *arg):
        if time.time() < self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.put_timer()