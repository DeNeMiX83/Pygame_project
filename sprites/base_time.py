import time

import pygame

from data.images.funk import load_image
from sprites.base_resize_sprite import BaseResize
from sprites.config import all_sprites, player_sprites


class BaseTime(BaseResize):
    def __init__(self, *group):
        super(BaseTime, self).__init__(*group)
        self.time_cur = time.time()
        self.time_tik = 0.2
        self.time_stop = 0

    def put_timer(self):
        self.time_cur = time.time()
        self.time_stop = self.time_cur + self.time_tik

    def update(self, *arg):
        if time.time() <= self.time_stop:
            return