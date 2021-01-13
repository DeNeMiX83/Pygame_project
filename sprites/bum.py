import time

import pygame
from data.config import size, width, height, FPS
from data.images.funk import load_image
from sprites.config import all_sprites, player_sprites


class Bum(pygame.sprite.Sprite):
    def __init__(self, ship, x, y):
        super(Bum, self).__init__(all_sprites)
        columns, rows = 5, 4
        self.frames = []
        self.cur_frame = 0
        sheet = load_image(['bum.png'], -1)
        self.cut_sheet(sheet, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.time_tik = 0.1
        self.put_timer()
        self.ship = ship

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
        if time.time() < self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.put_timer()
        if self.cur_frame == len(self.frames) - 1:
            self.ship.kill()