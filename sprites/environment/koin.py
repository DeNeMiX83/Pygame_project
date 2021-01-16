import time

import pygame

from data.images.funk import load_image
import game_things
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, player_sprites, menu_sprites


class Koin(BaseAnimateSprite):
    def __init__(self, x, y):
        super(Koin, self).__init__(all_sprites, menu_sprites)
        columns, rows = 3, 2
        sheet = load_image(['environment', 'koin.png'], -1)
        self.cut_sheet(sheet, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.radius = self.rect.w // 2 - 30
        self.rect.x = max(0, x - self.rect.w // 2)
        self.rect.y = max(0, y - self.rect.h // 2)
        self.time_tik = 0.1
        self.put_timer()

    def update(self, *arg):
        if pygame.sprite.spritecollideany(self, player_sprites, pygame.sprite.collide_circle):
            game_things.game_koins += 1
            self.kill()
        for ship in pygame.sprite.spritecollide(self, player_sprites, False,
                                                pygame.sprite.collide_circle_ratio(1.7)):
            d_x = ship.rect.x - self.rect.x
            d_y = ship.rect.y - self.rect.y
            if d_x >= 0:
                self.rect.x += 3
            if d_y >= 0:
                self.rect.y += 3
            if d_x <= 0:
                self.rect.x -= 3
            if d_y <= 0:
                self.rect.y -= 3
        if time.time() < self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.put_timer()
