import time

import pygame

from data.images.funk import load_image
from sprites.config import all_sprites, player_sprites


class Koin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Koin, self).__init__(all_sprites)
        columns, rows = 3, 2
        self.frames = []
        self.cur_frame = 0
        sheet = load_image(['environment', 'koin.png'], -1)
        self.cut_sheet(sheet, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.radius = self.rect.w // 2 - 30
        self.rect.x = max(0, x - self.rect.w // 2)
        self.rect.y = max(0, y - self.rect.h // 2)
        self.time_tik = 0.1
        self.put_timer()

    def put_timer(self):
        self.time_cur = time.time()
        self.time_stop = self.time_cur + self.time_tik

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *arg):
        if pygame.sprite.spritecollideany(self, player_sprites, pygame.sprite.collide_circle):
            self.kill()
        for ship in  pygame.sprite.spritecollide(self, player_sprites, False, pygame.sprite.collide_circle_ratio(1.7)):
            d_x = ship.rect.x - self.rect.x
            d_y = ship.rect.y - self.rect.y
            if d_x > 0:
                self.rect.x += 10
            if d_y > 0:
                self.rect.y += 10
        if time.time() < self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.put_timer()