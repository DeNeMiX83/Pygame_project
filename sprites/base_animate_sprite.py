import time

import pygame

from data.images.funk import load_image
from sprites.base_time import BaseTime
from sprites.config import all_sprites, player_sprites


class BaseAnimateSprite(BaseTime):
    def __init__(self, *group):
        super(BaseAnimateSprite, self).__init__(*group)
        columns, rows = 3, 2
        self.frames = []
        self.cur_frame = 0
        sheet = load_image(['environment', 'koin.png'], -1)
        # self.cut_sheet(sheet, columns, rows)
        # self.image = self.frames[self.cur_frame]

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
